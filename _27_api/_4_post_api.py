# https://jsonplaceholder.typicode.com/todos

import requests

url = "https://jsonplaceholder.typicode.com/todos"

request_body = {
    "rno" : 1,
    "name" : "Bharati"
}

response = requests.post(url,json=request_body).json()
print(response)