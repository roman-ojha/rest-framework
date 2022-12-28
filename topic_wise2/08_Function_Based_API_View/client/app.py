import requests
import json


def hello_world(url="http://127.0.0.1:8000/hw/"):
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.get(url=url, headers=headers)
    data = response.json()
    print(data)


# hello_world()


def h_w_post(url="http://127.0.0.1:8000/hwp/"):
    data = {
        'name': 'Roman'
    }
    headers = {
        'Content-Type': 'application/json'
    }
    json_data = json.dumps(data)
    response = requests.post(
        url=url, data=json_data, headers=headers)
    res_data = response.json()
    print(res_data)


# h_w_post()


def h_w_gp():
    hello_world("http://127.0.0.1:8000/hwgp/")
    h_w_post("http://127.0.0.1:8000/hwgp/")


# h_w_gp()


# CRUD Operation For Function based View
URL = "http://127.0.0.1:8000/crud/"


def read(id=None):
    data = {}
    if id is not None:
        data = {'id': id}

    json_data = json.dumps(data)

    # we have to provide header
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.get(url=URL, data=json_data, headers=headers)
    res_data = response.json()
    print(res_data)


# read()
# read(13)


def insert():
    data = {
        'name': 'Jack',
        'roll': 33,
        'city': 'Kathmandu'
    }
    headers = {
        "Content-Type": "application/json"
    }
    json_data = json.dumps(data)
    response = requests.post(url=URL, data=json_data, headers=headers)
    res_data = response.json()
    print(res_data)


# insert()


def update():
    def partial():
        data = {
            # passing partial update data
            'id': 14,
            'name': 'Harry',
            'city': 'NewYork'
        }
        headers = {
            "Content-Type": "application/json"
        }
        json_data = json.dumps(data)
        response = requests.put(url=URL, data=json_data, headers=headers)
        res_data = response.json()
        print(res_data)

    partial()

    def complete():
        data = {
            # passing complete update data
            'id': 6,
            'name': 'Razz',
            'roll': 30,
            'city': 'Pokhara'
        }
        headers = {
            "Content-Type": "application/json"
        }
        json_data = json.dumps(data)
        response = requests.patch(url=URL, data=json_data)
        res_data = response.json()
        print(res_data)

    # complete()


# update()


def delete():
    data = {
        'id': 12,
    }
    headers = {
        "Content-Type": "application/json"
    }
    json_data = json.dumps(data)
    response = requests.delete(url=URL, data=json_data, headers=headers)
    res_data = response.json()
    print(res_data)


# delete()
