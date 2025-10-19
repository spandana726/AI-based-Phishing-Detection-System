import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

def preprocess_data(input_csv, output_csv, scaler_path):
    df = pd.read_csv(input_csv)
    X = df.drop(columns=["URL", "Label"])
    y = df["Label"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    joblib.dump(scaler, scaler_path)
    df_scaled = pd.DataFrame(X_scaled, columns=X.columns)
    df_scaled["Label"] = y
    df_scaled.to_csv(output_csv, index=False)
    
    print(f"✅ Data preprocessed and saved to {output_csv}")
    print(f"✅ Scaler saved to {scaler_path}")


if __name__ == "__main__":
    preprocess_data("phishing_data_with_html_features.csv", "processed_data.csv", "scaler.pkl")

