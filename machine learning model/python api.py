from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
import pandas as pd
import joblib
import os
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)  

@app.route("/")
def home():
    return jsonify({"message": "Phishing Detection API is running!"})


try:
    model = tf.keras.models.load_model("phishing_detector_model.keras", compile=False)
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
except Exception as e:
    model = None
    print(f"Error loading model: {e}")


scaler_path = "scaler.pkl"
if os.path.exists(scaler_path):
    scaler = joblib.load(scaler_path)
    feature_names = list(scaler.feature_names_in_)
else:
    scaler = None
    feature_names = []
    print("Warning: 'scaler.pkl' not found. Scaling will not be applied!")

def extract_features(url):
    """Extract features from a given URL dynamically."""
    parsed_url = urlparse(url)
    features = {
        "length": len(url),
        "num_digits": sum(c.isdigit() for c in url),
        "num_special_chars": len([c for c in url if not c.isalnum()]),
        "num_subdomains": len(parsed_url.netloc.split(".")) - 1,
        "https": 1 if parsed_url.scheme == "https" else 0
    }
    
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        features["text_length"] = len(soup.get_text())
        features["num_links"] = len(soup.find_all("a"))
        features["num_scripts"] = len(soup.find_all("script"))
    except:
        features["text_length"] = 0
        features["num_links"] = 0
        features["num_scripts"] = 0

    return features

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded"}), 500
    if scaler is None:
        return jsonify({"error": "Scaler not found"}), 500

    try:
        data = request.json
        if "url" not in data:
            return jsonify({"error": "Missing 'url' in request"}), 400
        
        url = data["url"]
        features = extract_features(url)

        
        features_df = pd.DataFrame([features])

       
        if not set(feature_names).issubset(features_df.columns):
            return jsonify({"error": "Feature mismatch. Check extraction process."}), 400
        
       
        features_scaled = scaler.transform(features_df[feature_names])

        
        prediction = model.predict(features_scaled)[0][0]

        return jsonify({"phishing_probability": float(prediction)})

    except Exception as e:
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
