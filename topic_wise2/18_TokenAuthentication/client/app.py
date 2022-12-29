import requests
import json


# API to gettoken or to login
data = {
    # Providing 'username' & 'password'
    "username": "roman",
    "password": "roman"
}
json_data = json.dumps(data)

# we have to provide header
headers = {
    "Content-Type": "application/json"
}
URL = "http://127.0.0.1:8000/gettoken/"

response = requests.post(url=URL, data=json_data, headers=headers)
res_data = response.json()
print(res_data)
