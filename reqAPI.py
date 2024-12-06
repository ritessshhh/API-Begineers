import requests

# Base URL for the API
BASE_URL = "http://127.0.0.1:5000"

# Home Route
response = requests.get(f"{BASE_URL}/")
print("Home Route Response:", response.text)

# Current Time
response = requests.get(f"{BASE_URL}/time")
print("Current Time Response:", response.json())

# Current Date
response = requests.get(f"{BASE_URL}/date")
print("Current Date Response:", response.json())

# Greeting
response = requests.get(f"{BASE_URL}/greet/Ritesh")
print("Greeting Response:", response.json())

# API Status
response = requests.get(f"{BASE_URL}/status")
print("Status Response:", response.json())