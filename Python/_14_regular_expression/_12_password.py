import re 

password = input("Enter a strong password : ")
pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,16}$")
res = pattern.findall(password)
if res:
    print(password,"is a great password. Much secure")
else:
    print("Not a valid password. Please try again")