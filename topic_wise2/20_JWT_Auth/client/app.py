import requests
import json


def get_or_create_token():
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

    # Custom Generate Token class:
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
    URL = "http://127.0.0.1:8000/gettoken2/"

    response = requests.post(url=URL, data=json_data, headers=headers)
    res_data = response.json()
    print(res_data)

# get_or_create_token()


# This function will try to access the authenticated route by passing the token
def student_api():
    data = {
    }
    json_data = json.dumps(data)

    # We have to pass the 'Authentication' Header and pass generated validate user token
    headers = {
        "Authorization": "Token d8b1ad0a0a28d062b9e9ad2e6c76a0cd00155ade"
    }
    URL = "http://127.0.0.1:8000/studentapi/"

    response = requests.get(url=URL, headers=headers)
    res_data = response.json()
    print(res_data)


student_api()
