
import json
import random
import re


admins = []

class Admin:
    def __init__(self,name,number,email,password):
        self.admin_id = random.randint(1000, 9999)
        self.name = name
        self.number = number
        self.email = email
        self.password = password

def admin_input(prompt, pattern):
    while True:
        user_input = input(prompt)
        if re.match(pattern, user_input):
            print("Verified!!!")
            return user_input
        else:
            print("Invalid input!!")        

def register_admin():

    name = admin_input("Enter your full name: ", r"^[A-z]{2,15}$")
    number = admin_input("Enter your Mobile number: ", r"^[6789]\d{9}")
    email = admin_input("Enter your email: ", r"^\w+@[A-Za-z]+\.[A-Za-z]+$")
    password = admin_input("Create a password: ", r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*-_+=.,/;:?])[A-Za-z\d!@#$%^&*-_+=.,/;:?]{8,16}$")

    new_admin = Admin(name, number, email, password)
    admins.append(new_admin)
 



    new_admin = Admin(name,number,email,password)

    admins.append(new_admin)

    with open('admins.json', 'a') as file:
        admin_data = {
            'admin_id': new_admin.admin_id,
            'full_name': new_admin.name,
            'phone_number': new_admin.number,
            'email': new_admin.email,
            'password': new_admin.password
        }
        json.dump(admin_data, file)
        file.write('\n')

def login_admin():
    
    if not admins:
        print("No admin registered. Please register an admin first.")
        return None
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    for i in admins:
        if i.email == email and i.password == password:
            return i
    return None


students = []

class Student:
    def __init__(self,name,number,email,password):
        self.student_id = random.randint(1000, 9999)
        self.name = name
        self.number = number
        self.email = email
        self.password = password

def student_input(prompt, pattern):
    while True:
        user_input = input(prompt)
        if re.match(pattern, user_input):
            print("Verified!!!")
            return user_input
        else:
            print("Invalid input!!")

def register_student():

    name = student_input("Enter your full name: ", r"^[A-z]{2,15}$")
    number = student_input("Enter your Mobile number: ", r"^[6789]\d{9}")
    email = student_input("Enter your email: ", r"^\w+@[A-Za-z]+\.[A-Za-z]+$")
    password = student_input("Create a password: ", r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*-_+=.,/;:?])[A-Za-z\d!@#$%^&*-_+=.,/;:?]{8,16}$")

    new_student = Student(name, number, email, password)
    students.append(new_student)
    


    new_student = Student(name,number,email,password)
    students.append(new_student)
    with open('student.json', 'a') as file:
        student_data = {
            'student_id': new_student.student_id,
            'full_name': new_student.name,
            'phone_number': new_student.number,
            'email': new_student.email,
            'password': new_student.password
        }
        json.dump(student_data, file)
        file.write('\n')

    


def login_student():

    if not students:
        print("No student registered. Please register a student first.")
        return None
    
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    for i in students:
        if i.email == email and i.password == password:
            return i
    return None



if __name__ == "__main__":

    current_student = None

    current_admin = None

    while True:
        
        choice = input("Enter your choice: \n1.Login \n2.Register \n3.Exit \n")

        if choice == "1" :

            choice = input("\nEnter your choice:  \n1.Login as admin \n2.Login as user \n3.Exit \n")

            if choice == "1":
                current_admin = login_admin()
                if current_admin:
                    print("\nLogin successful!")
                else:
                    print("\nLogin failed.")

            elif choice == "2":
                current_student = login_student()
                if current_student:
                    print("\nLogin successful!")
                else:
                    print("\nLogin failed.")
            elif choice == "3":
                continue
            else:
                print("\nInvalid choice. Please try again.")

        elif choice == "2":
            choice = input("\nEnter your choice: \n1.Register as admin \n2.Register as userr \n3.Exit \n")

            if choice == "1":
                register_admin()
                print("\nRegister successful!")
            elif choice == "2":
                register_student()
                print("\nRegister successful!")
            elif choice == "3":
                continue
            else:
                print("\nInvalid choice. Please try again.")
        
        elif choice == "3":
             break
        else:
            print("\nInvalid choice. Please try again.")
MY_project_edyoda_replica.py
Share
Displaying MY_project_edyoda_replica.py.