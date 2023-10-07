import json

json_obj = """{
    "name":"Bharati",
    "female": true,
    "qualification": null,
    "morning":false
}"""

# convert your json object into dict
data = json.loads(json_obj)
print(data)
print(type(data))

# converts dict into json
json_obj = json.dumps(data)
print(json_obj)