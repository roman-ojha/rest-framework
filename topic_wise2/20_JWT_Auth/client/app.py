import requests
import json


# Function to get new Access & Refresh Token
def get_token():
    data = {
        "username": "roman",
        "password": "roman"
    }
    json_data = json.dumps(data)

    headers = {
        "Content-Type": "application/json"
    }
    URL = "http://127.0.0.1:8000/gettoken/"

    response = requests.post(url=URL, data=json_data, headers=headers)
    """
        Response:
        {'refresh': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3MjQwNjc4MywiaWF0IjoxNjcyMzIwMzgzLCJqdGkiOiIwOGViNjVlNGFlM2U0MDIwYTY5ZmU2ZDhjMmZlNzZkYiIsInVzZXJfaWQiOjF9.y0ONBZrbIVmwsxUZ8TaULfqyzy3YuiS1eig39mFqR9I',
        'access': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcyMzIwNjgzLCJpYXQiOjE2NzIzMjAzODMsImp0aSI6IjQ2ODM4OWU5MWU0MjRjYjQ5NTYyNGRiYzcxMzM0YzBmIiwidXNlcl9pZCI6MX0.E5J62-woJ8K_BElzGU5syyu6NLBGY9jXvKkJfagZZ6Q'}
    """
    res_data = response.json()
    print(res_data)


# get_token()


# Function to verify the token provide by server
def verify_token():
    data = {
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcyMzIxMDkxLCJpYXQiOjE2NzIzMjAzODMsImp0aSI6IjkzNmNhMGY1NjhmYzQ0YjI5NTBjYWZkZGE1ZjZiODY2IiwidXNlcl9pZCI6MX0.r0PX5fBpB6Mw7zobcWtl9vmMSiXJp1-_f4n_kIWnr58",
    }
    json_data = json.dumps(data)

    headers = {
        "Content-Type": "application/json"
    }
    URL = "http://127.0.0.1:8000/verifytoken/"

    response = requests.post(url=URL, data=json_data, headers=headers)
    # Response 200 status if verified
    res_data = response.json()
    print(res_data)


# verify_token()

# Function to refresh Access Token by providing Refresh Token


def refresh_token():
    data = {
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3MjQwNjc4MywiaWF0IjoxNjcyMzIwMzgzLCJqdGkiOiIwOGViNjVlNGFlM2U0MDIwYTY5ZmU2ZDhjMmZlNzZkYiIsInVzZXJfaWQiOjF9.y0ONBZrbIVmwsxUZ8TaULfqyzy3YuiS1eig39mFqR9I",
    }
    json_data = json.dumps(data)

    headers = {
        "Content-Type": "application/json"
    }
    URL = "http://127.0.0.1:8000/refreshtoken/"

    response = requests.post(url=URL, data=json_data, headers=headers)
    # Response 200 status if verified
    res_data = response.json()
    print(res_data)


# refresh_token()


# Function to access api using Access token
def student_api():
    # We have to pass the 'Authentication' Header and pass generated validate user token
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcyMzIxNjE0LCJpYXQiOjE2NzIzMjAzODMsImp0aSI6IjYzZTg1ZTU3ZTY2OTQxY2M5ODllYWRhODI0NzM0MjY0IiwidXNlcl9pZCI6MX0.BTe3j3p4aOeZG86IP_jDsDTlrrQ9IwnCtdPeRXgu3XE"
    }
    URL = "http://127.0.0.1:8000/studentapi/"

    response = requests.get(url=URL, headers=headers)
    res_data = response.json()
    print(res_data)


student_api()
