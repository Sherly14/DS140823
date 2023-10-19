import json

def register(filename,id,name,mobile,email,password):
    details = {
        "ID ": id,
        "Name ": name,
        "Mobile No. ": mobile,
        "Email" : email,
        "Password" : password
    }

    with open(filename,"r+") as file:
        try:
            data = json.load(file)
            if details not in data:
                data.append(details)
                file.seek(0)
                file.truncate() # clear the file
                json.dump(data,file)
                return True
        except Exception as ex:
            return False

def login():
    pass