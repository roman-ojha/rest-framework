import requests
import json


# Function to read data if we pass id then get the specific data rather get list of data
def read(id=None):
    URL = ""
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
