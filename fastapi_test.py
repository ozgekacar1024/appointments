import requests

# Replace with your API endpoint URL
url = "http://127.0.0.1:8000/create_branch"

data = {
    "name": "value1",  # Replace with your first string argument
    "location": "value2",   # Replace with your second string argument
    "frenchise": "value3"
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Request successful. Response:", response.json())
else:
    print("Request failed. Status code:", response.status_code)