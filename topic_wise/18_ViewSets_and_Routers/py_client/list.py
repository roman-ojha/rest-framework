from email import header
import requests
from auth import authUser

auth_user_res = authUser()

if auth_user_res.status_code == 200:
    token = auth_user_res.json()['token']
    headers = {
        "Authorization": f"Bearer {token}"
    }
    print(headers)
    endpoint = "http://localhost:8000/api/products/list"
    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())
