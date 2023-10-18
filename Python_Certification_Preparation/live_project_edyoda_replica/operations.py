import json

def register(filename,student_id,name,mobile,email,password):
    details = {
        "ID ": student_id,
        "Name ": name,
        "Mobile No. ": mobile,
        "Email" : email,
        "Password" : password
    }

    with open(filename,"w") as file:
        json.dump(details,file)