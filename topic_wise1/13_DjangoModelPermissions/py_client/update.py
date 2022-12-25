import requests

endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    # data contain the field that we want to update
    "title": "Hello world my old friend",
    "price": 138.94
}

# now we will use 'put' method to update data
get_response = requests.put(endpoint, json=data)
print(get_response.json())
