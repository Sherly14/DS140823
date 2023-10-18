from operations import register
import random
import re

# class Main:

#     def execute(self,choice):
        
#         if  choice == 1:
#             print("******************Admin Login******************")
#             ch='1: Login \n2: Register\n3: Exit'
#             if ch==1:
#                 username=input('Enter Username : ')
#                 password=input('Enter Password : ')
#             elif ch==2:
#                 student_id=random.randint(1,10000)
#                 name=input('Enter name : ')
#                 mobile=int(input('Enter phone number  : '))
#                 email=input('Enter email : ')
#                 password=input('Enter password : ')
#                 name_res=re.findall(r'^[a-zA-Z]+\\.?',name)
#                 email_res = re.findall(r"^([A-z0-9]+[._])*[A-z0-9]+@[a-z]+(.[a-z]{2,})+$",email) 
#                 mobile_res= re.findall(r'^[+91 ]{4}[6-9]{1}[0-9]{9}$',mobile)
#                 password_res=re.findall(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,16}$",password)
#                 arr=[name_res,email_res,mobile_res,password_res]
#                 if False not in arr :
#                     pass
#                 else:
#                     for i in arr:
#                         if i ==False:
#                             print (f'Invalid {i} ')
#                     self.execute(1)
#             else:
#                 exit(1)

#         elif choice == 2:
#             print("******************Student Login******************")
#             ch='1: Login \n2: Register\n3: Exit'
#             if ch==1:
#                 username=input('Enter Username : ')
#                 password=input('Enter Password : ')
#             elif ch==2:
#                 student_id=random.randint(1,10000)
#                 name=input('Enter name : ')
#                 mobile=int(input('Enter phone number  : '))
#                 email=input('Enter email : ')
#                 password=input('Enter password : ')
#                 name_res=re.findall(r'^[a-zA-Z]+\\.?',name)
#                 email_res = re.findall(r"^([A-z0-9]+[._])*[A-z0-9]+@[a-z]+(.[a-z]{2,})+$",email) 
#                 mobile_res= re.findall(r'^[+91 ]{4}[6-9]{1}[0-9]{9}$',mobile)
#                 password_res=re.findall(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,16}$",password)
#                 arr=[name_res,email_res,mobile_res,password_res]
#                 if False not in arr :
#                     pass
#                 else:
#                     for i in arr:
#                         if i ==False:
#                             print (f'Invalid {i} ')
#                     self.execute(1)
#             else:
#                 exit(1)
#         else:
#             exit(1)
        

if __name__ == "__main__":
    
    # main = Main()

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

        if choice == 2:
            try:
                register_choice = int(input(" \n1.Register as Student \n2.Register as Admin \n3.Exit : \n"))
            except ValueError:
                print("Please enter valid choice!")
                continue

            if register_choice == 1:
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
                    register("Student.json",student_id,name,email,mobile,password)
                    
                else:
                    for i, result in enumerate(validation_results):
                        if result is None:
                            print(f'Invalid input for "Name", "Email", "Mobile", "Password"{[i]}')
                
                

                    
        
        
        
        
        
        
        
        # main.execute(1)