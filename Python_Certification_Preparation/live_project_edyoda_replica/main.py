from operations import register,login,add_module,view_module,update_module,delete_module
import random
import re

if __name__ == "__main__":

    while True:
        try:
            choice = int(input("Enter  \n1.Login \n2.Register \n3.Exit : \n"))
        except ValueError:
            print("Please enter valid choice!")
            continue

        if choice == 1:
            try:
                login_choice = int(input(" \n1.Login as Student \n2.Login as Admin \n3.Exit : \n"))
            except ValueError:
                print("Please enter valid choice!")
                continue

            if login_choice == 1:
                print("****************Login as Student**************")
                email_ID = input("Enter your email ID : ")
                password = input("Enter your password : ")
                login_flag = login("Student.json",email_ID,password)
                print("Successfully Logged In!!!") if login_flag else print("Log In Failed!!!")

            elif login_choice == 2:
                print("****************Login as Admin**************")
                email_ID = input("Enter your email ID : ")
                password = input("Enter your password : ")
                login_flag = login("Admin.json",email_ID,password)

                if login_flag:
                    while True:
                        admin_choice = int(input("Enter \n1.Create Module \n2.View Module \n3.Update Module \n4.Delete Module \n5.Exit : \n"))

                        if admin_choice == 1:
                            print("*****************Create Module******************")
                            module_ID = random.randint(1, 10000)
                            module_name = input("Enter Module Name : ")
                            start_date = input("Enter start date : ")
                            end_date = input("Enter end date : ")
                            
                            size = int(input("Enter total topics you want to add : "))
                            module_topic = []
                            for i in range(size):
                                topic = input("Enter topic : ")
                                module_topic.append(topic)

                            module_flag = add_module("Module.json",module_ID,module_name,start_date,end_date,module_topic)
                            print("Successfully Added!!!") if module_flag else print("Module Adding Failed!!!")

                        elif admin_choice == 2:
                            print("*****************View Module******************")
                            data = view_module("Module.json")
                            for i in data:
                                print('Module ID : ',i['ID '])
                                print('Module Name : ',i['Module Name '])
                                print('Module Start Date : ',i['Start Date '])
                                print('Module End Date : ',i['End Date '])
                                ctr = 0
                                for topic in i['Module Topic']:
                                    ctr+=1
                                    print(f'Module Topic {ctr} : ',topic)
                                print()

                        elif admin_choice == 3:
                            print("*****************Update Module******************")
                            module_ID =  int(input("Enter Module ID : "))
                            module_name = input("Enter Module Name : ")
                            start_date = input("Enter start date : ")
                            end_date = input("Enter end date : ")
                            
                            size = int(input("Enter total topics you want to add : "))
                            module_topic = []
                            for i in range(size):
                                topic = input("Enter topic : ")
                                module_topic.append(topic)

                            update_flag = update_module("Module.json",module_ID,module_name,start_date,end_date,module_topic)
                            print("Successfully Updated!!!") if update_flag else print("Module Updation Failed!!!")

                        elif admin_choice == 4:
                            print("*****************Delete Module******************")
                            module_ID =  int(input("Enter Module ID : "))
                            delete_flag = delete_module("Module.json",module_ID)
                            print("Successfully Deleted!!!") if delete_flag else print("Module Deletion Failed!!!")
                        else:
                            exit(1)

                else: print("Log In Failed!!!")

            else:
                exit(1)
                

        if choice == 2:
            try:
                register_choice = int(input(" \n1.Register as Student \n2.Register as Admin \n3.Exit : \n"))
            except ValueError:
                print("Please enter valid choice!")
                continue

            if register_choice == 1:
                print("****************Student Registration**************")
                student_id = random.randint(1, 10000)
                name = input('Enter name: ')
                mobile = input('Enter phone number: ')
                email = input('Enter email: ')
                password = input('Enter password: ')

                name_res = re.match(r'^[a-zA-Z]+\.?$', name)
                email_res = re.match(r'^([A-z0-9]+[._])*[A-z0-9]+@[a-z]+(\.[a-z]{2,})+$', email)
                mobile_res = re.match(r'^[+91 ]{4}[6-9]{1}[0-9]{9}$', mobile)
                password_res = re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,16}$', password)

                validation_results = [name_res, email_res, mobile_res, password_res]
                if all(validation_results):
                    register_flag = register("Student.json",student_id,name,mobile,email,password)
                    print("Successfully Registered!!!") if register_flag else print("Registration Failed!!!")
                else:
                    for i, result in enumerate(validation_results):
                        if result is None:
                            print(f'Invalid input for "Name", "Email", "Mobile", "Password"{[i]}')

            elif register_choice == 2:
                print("****************Admin Registration**************")
                admin_id = random.randint(1, 10000)
                name = input('Enter name: ')
                mobile = input('Enter phone number: ')
                email = input('Enter email: ')
                password = input('Enter password: ')

                name_res = re.match(r'^[a-zA-Z]+\.?$', name)
                email_res = re.match(r'^([A-z0-9]+[._])*[A-z0-9]+@[a-z]+(\.[a-z]{2,})+$', email)
                mobile_res = re.match(r'^[+91 ]{4}[6-9]{1}[0-9]{9}$', mobile)
                password_res = re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,16}$', password)

                validation_results = [name_res, email_res, mobile_res, password_res]
                if all(validation_results):
                    register_flag = register("Admin.json",admin_id,name,mobile,email,password)
                    print("Successfully Registered!!!") if register_flag else print("Registration Failed!!!")
                else:
                    for i, result in enumerate(validation_results):
                        if result is None:
                            print(f'Invalid input for "Name", "Email", "Mobile", "Password"{[i]}')

            else:
                exit(1)


        else:
            exit(1)
                
                

                    
        
        
        
        
        
        