import re

data = input("enter your mobile number: ")
pattern = re.compile(r"^[+91 ]{4}[6-9]{1}[0-9]{9}$")
res = pattern.findall(data)
print(res)
if res:
    print("Format is correct")
else:
    print("Format is incorrect")