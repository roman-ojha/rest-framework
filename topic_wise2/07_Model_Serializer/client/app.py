import requests
import json

# For Function based View
URL = "http://127.0.0.1:8000/crud/"

# For class Based View
# URL = "http://127.0.0.1:8000/class-crud/"


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


# read()
# read(5)


def insert():
    data = {
        'name': 'Roman',
        'roll': 35,
        'city': 'Kathmandu'
    }
    json_data = json.dumps(data)
    response = requests.post(url=URL, data=json_data)
    res_data = response.json()
    print(res_data)


# insert()


def update():
    def partial():
        data = {
            # passing partial update data
            'id': 5,
            'name': 'Harry',
            'city': 'NewYork'
        }
        json_data = json.dumps(data)
        response = requests.put(url=URL, data=json_data)
        res_data = response.json()
        print(res_data)

    # partial()

    def complete():
        data = {
            # passing complete update data
            'id': 6,
            'name': 'Razz',
            'roll': 30,
            'city': 'Pokhara'
        }
        json_data = json.dumps(data)
        response = requests.patch(url=URL, data=json_data)
        res_data = response.json()
        print(res_data)

    complete()


update()


def delete():
    data = {
        'id': 5,
    }
    json_data = json.dumps(data)
    response = requests.delete(url=URL, data=json_data)
    res_data = response.json()
    print(res_data)


# delete()
