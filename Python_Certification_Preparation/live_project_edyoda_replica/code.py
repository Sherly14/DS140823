# venkat : https://filetransfer.io/data-package/hvbgTa0J#link
# vinu
def login(self, username, password, role):
        if (
            username in self.users
            and self.users[username]["password"] == password
            and self.users[username]["role"] == role
            and re.search(r"[!@#$%^&*]", password)
        ):
            print("Login successful!")
        else:
            raise Exception("Login failed. Please check your credentials.")
        
import random
import re

class EdyodaUserManager:
    def __init__(self):
        self.users = {}

    def generate_user_id(self):
        return random.randint(1000, 9999)

    def register(self, role):
        print(f"Register as {role}")
        name = input("Name: ")
        mobile = input("Mobile: ")
        email = input("Email: ")
        password = input("Password: ")

        if not self.validate_user_data(name, mobile, email, password):
            print("Invalid data. Registration failed.")
            return

        user_id = self.generate_user_id()
        self.users[email] = {
            "user_id": user_id,
            "name": name,
            "mobile": mobile,
            "email": email,
            "password": password,
            "role": role,
        }
        print("Registration successful! User ID:", user_id)
        return user_id
    
# shubha 
import re
class edyoda():
    def execute(self,choice):
        if choice == 1:
            print("********Login******")
            login_choice = int(input("1.Login as Admin \n2.Login as student \n3.Exit\n"))
            if login_choice == 1:
                    print("$$$$Login as Admin$$$$")

                    user_name = input("Enter username:")
                    check_username = re.findall(r"^[A-z]{2,15}$",user_name)
                    if check_username:
                          print("Valid user name ")
                    else:
                          print("Invalid username")
                    
                    pass_word = input("Enter your password:")
                    pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*-_+=.,/\;:?])[A-Za-z\d!@#$%^&*-_+=.,/\;:?]{8,16}$")
                    res = pattern.findall(pass_word)
                  
                    if res:
                        print(pass_word,"is valid and strong")
                    else: