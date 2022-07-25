import requests

# different endpoint that will response base some data
endpoint = "http://httpbin.org/"
endpoint = "http://httpbin.org/anything"

# now we will use requests package to fetch the data from the endpoint
# REST APIs -> Web based API
# so it need http request
get_response = requests.get(endpoint)
# HTTP Request -(give)> HTML
# Rest API HTTP request -(give)> JSON | XML
print(get_response.text)  # return in JSON Formate
print(get_response.json())  # return python dictionary
# return status code for that specific request
print(get_response.status_code)
# print(requests.get(endpoint, json={"query": "Hello world"}).json())

# requesting django endpoint
django_endpoint = "http://localhost:8002/"
print(requests.get(django_endpoint).status_code)
