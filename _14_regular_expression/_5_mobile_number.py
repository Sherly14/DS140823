import re 
mobile_number = input("Enter your mobile_number:")
res = re.findall(r"^[+91]{3}[1-9]{1}[0-9]{9}$",mobile_number) 
print(res)
if res:
    print(mobile_number,"is valid")
else:
    print(mobile_number, "is not valid")