import requests
from getpass import getpass

# because we want to use it on other file to get authenticate we will going to define it we function


def authUser():
    auth_endpoint = "http://localhost:8000/api/auth/"
    username = input("username: ")
    password = getpass()
    # getpass will ask user for password

    auth_response = requests.post(
        auth_endpoint, json={"username": username, "password": password})
    # now here we are sending username and password to get authenticate

    # we will get token as response
    return auth_response
