from itertools import product
from turtle import goto
import requests

product_id = input("Enter Product Id to delete: ")
try:
    product_id = int(product_id)
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"
    get_response = requests.delete(endpoint)
    print(get_response.status_code, get_response.status_code == 204)
    # after delete we will get status_code
except:
    print("Given Id is not a number")
