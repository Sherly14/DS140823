import json
import os

def register(filename,id,name,mobile,email,password):
    details = {
        "ID ": id,
        "Name ": name,
        "Mobile No. ": mobile,
        "Email" : email,
        "Password" : password
    }

    if not os.path.exists(filename):
        open(filename,"x")
    with open(filename,"r+") as file:
        try:
            data = json.load(file)
            if details not in data:
                data.append(details)
                file.seek(0)
                file.truncate() # clear the file
                json.dump(data,file)
                return True
        
        except json.decoder.JSONDecodeError as ex:
            lst = []
            lst.append(details)
            json.dump(lst,file)
            return True
        
        except Exception as ex:
            return False

def login(filename,email_ID,password):
    with open(filename,"r") as file: 
        try:
            data = json.load(file)
            for i in data:
                if i["Email"] == email_ID and i["Password"] == password:
                    return True
                else:
                    return False
        except Exception as ex:
            print(ex)
            return False

          
def add_module(filename,module_ID,module_name,start_date,end_date,module_topic):
    details = {
        "ID ": module_ID,
        "Module Name ": module_name,
        "Start Date ": start_date,
        "End Date " : end_date,
        "Module Topic" : module_topic
    }

    if not os.path.exists(filename):
        open(filename,"x")
    with open(filename,"r+") as file:
        try:
            data = json.load(file)
            if details not in data:
                data.append(details)
                file.seek(0)
                file.truncate() # clear the file
                json.dump(data,file)
                return True
        
        except json.decoder.JSONDecodeError as ex:
            lst = []
            lst.append(details)
            json.dump(lst,file)
            return True
        
        except Exception as ex:
            return False
        

def view_module():
    try:
        with open('Module.json','r') as rawdata:
            try:
                data=json.load(rawdata)
            except json.decoder.JSONDecodeError as je:
                print("No data in file !")
            for i in data:
                print('Module ID : ',i['ID '])
                print('Module Name : ',i['Module Name '])
                print('Module Start Date : ',i['Start Date '])
                print('Module End Date : ',i['End Date '])
                ctr =0
                for topic in i['Module Topic']:
                    ctr+=1
                    print(f'Module Topic {ctr} : ',topic)
                print()
    except:
        print('no file found')


def update_module():
    pass