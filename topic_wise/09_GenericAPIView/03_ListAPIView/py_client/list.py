import requests

endpoint = "http://localhost:8000/api/products/list"
data = {
    "title": "This field is done"
}
get_response = requests.get(endpoint)
print(get_response.json())
