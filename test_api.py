import requests

# Define API URL
url = "http://127.0.0.1:5000/predict"

# Create a sample request with 453 feature values
data = {str(i): [0.5] for i in range(453)}  # 453 features, all with value 0.5

print(" Sending request to Flask API...")
response = requests.post(url, json=data)

print(" Request sent!")
print("Response Status Code:", response.status_code)
print("Response JSON:", response.json())  
