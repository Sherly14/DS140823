import json

with open(r"C:\Users\vashi\OneDrive\Documents\GitHub\DS140823\_23_json_file_handling\demo.json") as file:
    
    # reading json file and converting json data into dict
    data = json.load(file)
    print(data)
    print(type(data))


with open(r"C:\Users\vashi\OneDrive\Documents\GitHub\DS140823\_23_json_file_handling\test.json","w") as file:
    data = {
        "rno":1,
        "name":"Raj",
        "male":True
    }
    # converted dict into json and stored it inside json file
    json.dump(data,file)
