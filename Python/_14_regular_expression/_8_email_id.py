import re 
email_id = input("Enter your email_id: ")
res = re.findall(r"^([A-z0-9]+[._])*[A-z0-9]+@[a-z]+(.[a-z]{2,})+$",email_id) 
print(res)
if res:
    print(email_id,"valid")
else:
    print(email_id, "invalid")


