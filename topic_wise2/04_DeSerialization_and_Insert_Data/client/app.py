import requests
import json

URL = "http://127.0.0.1:8000/insert/"

# Inserting data
data = {
    'name': 'Razz',
    'roll': 25,
    'city': 'Kathmandu'
}

# Now we will Convert python object into JSON data
json_data = json.dumps(data)

# Requesting to insert data
response = requests.post(url=URL, data=json_data)
data = response.json()
print(data)
