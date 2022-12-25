from cgi import print_exception
import requests

endpoint = "http://localhost:8000/api/"
get_response = requests.post(
    endpoint, json={"title": "Roman", "content": "Hello Roman", "price": 12})
print(get_response.json())
print(get_response.headers)
print(get_response.status_code)
