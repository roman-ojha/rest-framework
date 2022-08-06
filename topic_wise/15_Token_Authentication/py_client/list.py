import requests
from auth import authUser

# first we will auth user
auth_user_res = authUser()
print(auth_user_res.json())

if auth_user_res.status_code == 200:
    endpoint = "http://localhost:8000/api/products/list"
    data = {
        "title": "This field is done"
    }
    get_response = requests.get(endpoint)
    print(get_response.json())
