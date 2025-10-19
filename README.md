# 🛡️ AI-Based Phishing Detection System

## 🔍 Overview
The **AI-Based Phishing Detection System** is an intelligent machine learning project designed to detect whether a website is **phishing** or **legitimate**.  
It uses **URL-based**, **HTML-based**, and **NLP-based** features to classify websites with high accuracy.  
A **Chrome extension** is integrated with the model to provide real-time website safety analysis for users while browsing.

---

## 🧠 Workflow
1. **Data Collection:** Phishing and legitimate URLs are gathered from verified datasets.  
2. **Feature Extraction:** Features are derived from URLs, HTML code, and textual data.  
3. **Model Training:** A neural network model is trained using Keras/TensorFlow.  
4. **Prediction API:** The trained model is deployed through a Python API (Flask/FastAPI).  
5. **Chrome Extension:** The extension interacts with the API to classify websites instantly.

---

## 📁 Folder Structure
```
AI-Phishing-Detection/
│
├── pycache/
├── feature_extraction.py
├── NLP_analysis.py
├── process.py
├── mlmodel.py
├── phishing_data.xlsx
├── phishing_data_with_features.xlsx
├── phishing_data_with_html_features.xlsx
├── phishing_dataset.py
├── phishing_detector_model.h5
├── phishing_detector_model.keras
├── processed_data.xlsx
├── scaler.pkl
├── python api.py
│
├── chrome_extension/
│ ├── manifest.json
│ ├── popup.html
│ ├── popup.js
│ ├── styles.css
│
└── README.md
```

---

## ⚙️ Installation and Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/<your-username>/AI-Phishing-Detection.git
cd AI-Phishing-Detection
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate    # for Windows
# or
source venv/bin/activate   # for Mac/Linux
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

If you don’t have a requirements file, install manually:
```bash
pip install tensorflow scikit-learn pandas numpy flask requests beautifulsoup4 nltk joblib
```

---

## ▶️ Running the Project

### Step 1: Start the API Server
Run the backend model API:
```bash
python "python api.py"
```
It will start the local server at:
```
http://127.0.0.1:5000/predict
```

### Step 2: Use the Chrome Extension
1. Open Chrome and go to `chrome://extensions/`
2. Turn on **Developer Mode**
3. Click **Load Unpacked**
4. Select the folder containing:
   - manifest.json  
   - popup.html  
   - popup.js  
   - styles.css  
5. The extension will appear in your browser toolbar.

When you visit a website, the extension will send the URL to your API and display:
- ✅ Legitimate  
- 🚨 Phishing  

---

## 🧾 Example API Response
```json
{
  "url": "http://secure-paypal-login.com",
  "prediction": "Phishing",
  "confidence": 0.94
}
```

---

## 🧩 Technologies Used
- Python, TensorFlow, Scikit-learn  
- Flask/FastAPI  
- Pandas, NumPy, BeautifulSoup4  
- NLP (NLTK)  
- Chrome Extension (HTML, CSS, JS, Manifest v3)

---

## 🧪 Model Files
- `phishing_detector_model.h5` / `.keras` – Trained neural network  
- `scaler.pkl` – StandardScaler for feature normalization  
- `processed_data.xlsx` – Final dataset after cleaning  
- `feature_extraction.py` – Script for generating URL & HTML features  

---

## 📜 Future Enhancements
- Real-time visual similarity detection (screenshot analysis)  
- Cloud-based API deployment  
- Integration with email phishing detection  
- Automatic dataset updates using threat feeds  

---

## 👩‍💻 Author
**Spandana Gunaganti**  
📧 Email: gunagantispandana@gmail.com
💻 GitHub: https://github.com/spandana726

---

## 🪪 License
This project is licensed under the **MIT License**.
