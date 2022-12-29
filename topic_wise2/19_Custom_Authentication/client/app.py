import requests
import json


def custom_auth():
    URL = "http://127.0.0.1:8000/studentapi/?username=roman"

    response = requests.get(url=URL)
    res_data = response.json()
    print(res_data)


custom_auth()
