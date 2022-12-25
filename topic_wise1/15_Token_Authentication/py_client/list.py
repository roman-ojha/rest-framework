from email import header
import requests
from auth import authUser

# first we will auth user
auth_user_res = authUser()

if auth_user_res.status_code == 200:
    # we will extract that response token value
    token = auth_user_res.json()['token']
    # and we will add authorization header and pass token
    headers = {
        # "Authorization": f"Token {token}"
        # NOTE: 'Token' is the rest framework common keyword get authorization
        "Authorization": f"Bearer {token}"
    }
    print(headers)
    endpoint = "http://localhost:8000/api/products/list"
    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())
