from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("spectral_model.pkl")

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()  # Receive input JSON
        df = pd.DataFrame(data)  # Convert JSON to DataFrame
        df.columns = df.columns.astype(str)
        if df.shape[1] != 453:  # Check if input has the right number of features
            return jsonify({"error": f"Feature shape mismatch, expected: 453, got {df.shape[1]}"})
        predictions = model.predict(df)  # Make predictions
        return jsonify({"predictions": predictions.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    print("Flask API is starting...")
    app.run(debug=True)  # Runs on localhost:5000
