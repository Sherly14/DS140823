#  pip install requests

import requests

url = "http://ip.jsontest.com/"

response = requests.request("GET",url).json()
print(response)

