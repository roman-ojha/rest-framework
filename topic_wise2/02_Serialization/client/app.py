import requests

URL = "http://localhost:8000/detail/"
response = requests.get(url=URL)
data = response.json()
print(data)
