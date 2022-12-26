import requests
import json

URL = "http://127.0.0.1:8000/crud/"

# Function to read data if we pass id then get the specific data rather get list of data


def read(id=None):
    data = {}
    if id is not None:
        data = {'id': id}

    # converting python dict into JSON
    json_data = json.dumps(data)

    # requesting
    response = requests.get(url=URL, data=json_data)
    res_data = response.json()
    print(res_data)


def insert():
    pass


read(1)
