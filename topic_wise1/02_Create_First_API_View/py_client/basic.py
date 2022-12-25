import requests

# Requesting to the endpoint that we just create
endpoint = "http://localhost:8000/api"
get_response = requests.get(endpoint)
print(get_response.json())
