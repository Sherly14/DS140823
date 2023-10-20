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
        

def view_module(filename):
    try:
        with open(filename,'r') as rawdata:
            try:
                data=json.load(rawdata)
                return data
            except json.decoder.JSONDecodeError as je:
                print("No data in file !")
    except:
        print('no file found')


# def update_module(moudleid,start_date,end_date,module_topic:list):
#     data = view_module()
#     if not data:
#         print('No Modules Present ! Create Module first')
#     else:
#         for i in data:
#             if i['ID ']==moudleid:
#                 module_ID=i['ID ']
#                 module_name=i['Module Name ']
#                 data.remove(i)
#                 details = {
#                         "ID ": module_ID,
#                         "Module Name ": module_name,
#                         "Start Date ": start_date,
#                         "End Date " : end_date,
#                         "Module Topic" : module_topic
#                      }
#                 data.append(details)
#                 with open('Module.json','w')as rfile:
#                     try:
#                         json.dump(data,rfile)
#                     except json.decoder.JSONDecodeError as e:
#                         try:
#                             ch=int(input('no modules found! press 1 to add one  ')) 
#                             if ch==1:
#                                 module_flag = add_module("Module.json",module_ID,module_name,start_date,end_date,module_topic)
#                                 print("Successfully Added!!!") if module_flag else print("Module Adding Failed!!!")
#                             else:
#                                 return False
#                         except:
#                             print("no modules found! plz check file ")
#                 print("Successfully Added!!!") if 1==1 else print("Module Adding Failed!!!")       
#                 break


def update_module(filename,module_ID,module_name,start_date,end_date,module_topic):
    file = open(filename,"r+")
    data = json.load(file)
    for i in range(len(data)):
        if data[i]["ID "] == module_ID:
            data[i]["Module Name "] = data[i]["Module Name "]
            data[i]["Start Date "] = start_date
            data[i]["End Date "] = end_date
            data[i]["Module Topic"].extend(module_topic)
            file.seek(0)
            file.truncate()
            json.dump(data,file,indent=4)
            file.close()
            return True
    else:
        add_module(filename,module_ID,module_name,start_date,end_date,module_topic)  
    return False


def delete_module(filename,module_ID):
    file = open(filename,"r+")
    data = json.load(file)
    for i in range(len(data)):
        if data[i]["ID "] == module_ID:
            data.pop(i)
            file.seek(0)
            file.truncate()
            json.dump(data,file,indent=4)
            file.close()
            return True
    return False