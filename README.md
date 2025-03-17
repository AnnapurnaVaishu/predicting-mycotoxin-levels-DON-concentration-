# 🌽 Machine Learning Pipeline for Vomitoxin Prediction

This repository contains a **machine learning pipeline** for predicting **vomitoxin levels in corn** using spectral data. The project covers **data preprocessing, model training, evaluation, and API deployment**.

---

## 📌 1. Project Structure  
```
ML_Assignment/
│── ML_ASSIGNMENT.ipynb        # Jupyter Notebook with entire pipeline
│── app.py                     # Flask API for model predictions
│── test_api.py                 # Script to test the API
│── spectral_model.pkl         # Trained ML model file
│── datasets/                  # Folder containing datasets
│   ├── original_dataset.csv
│   ├── preprocessed_dataset.csv
│   ├── actual_vs_predicted.csv
│── README.md                   # Setup instructions (this file)
│── requirements.txt             # List of dependencies
└── .gitignore                   # Ignore unnecessary files
```

---

## 📌 2. Setup Instructions  
### 🔹 Step 1: Clone the Repository  
```sh
git clone https://github.com/YOUR_USERNAME/ML_Assignment.git
cd ML_Assignment
```

### 🔹 Step 2: Create a Virtual Environment (Optional)  
```sh
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 🔹 Step 3: Install Dependencies  
```sh
pip install -r requirements.txt
```
---

## 📌 3. Running the Code  
### 🔹 Open and Run the Jupyter Notebook  
- Open `ML_ASSIGNMENT.ipynb` in Jupyter Notebook or VS Code.  
- Run all cells to see **data preprocessing, model training, and evaluation**.

---

## 📌 4. Running the Flask API  
### 🔹 Start the API Server  
```sh
python app.py
```
✅ If the API runs successfully, it will show:  
```
 * Running on http://127.0.0.1:5000/
```

### 🔹 Test the API Using Python (`test_api.py`)  
```python
import requests

url = "http://127.0.0.1:5000/predict"
data = {str(i): [0.5] for i in range(453)}  # 453 feature values

response = requests.post(url, json=data)
print(response.json())  # Model predictions
```

### 🔹 Test the API Using Postman  
1. **Set request type to** `POST`  
2. **Enter URL:** `http://127.0.0.1:5000/predict`  
3. **Go to "Body" → raw → JSON** and input:
   ```json
   {
       "0": [0.5], "1": [0.5], "2": [0.5]
   }
   ```
4. **Click "Send"** → You should see predictions.

---

## 📌 5. Datasets  
- **Original Dataset:** `datasets/original_dataset.csv` (Raw data before preprocessing)  
- **Preprocessed Dataset:** `datasets/preprocessed_dataset.csv` (Cleaned & transformed data)  
- **Actual vs. Predicted:** `datasets/actual_vs_predicted.csv` (Model performance evaluation)  

---

## 📌 6. Model Training & Evaluation  
- The model was trained using **XGBoost** and evaluated using:  
  - **Mean Absolute Error (MAE):** 6.51  
  - **Mean Squared Error (MSE):** 378.18  
  - **R² Score:** 0.9999  
- The trained model is saved as `spectral_model.pkl`.  

---

## 📌 7. Deployment (Optional)  
To deploy the model via **Flask API**:
```sh
python app.py
```
For **Docker deployment**:
```sh
docker build -t ml-assignment .
docker run -p 5000:5000 ml-assignment
```
This will make the API accessible at `http://127.0.0.1:5000/predict`.

---

## 📌 8. Key Findings & Future Improvements  
- ✅ **High prediction accuracy (R² Score: 0.9999)**  
- ✅ **Feature selection & log transformation improved performance**  
- 🔹 **Future improvements:** Deploy to cloud (AWS/GCP), interpretability with SHAP/LIME  

---

