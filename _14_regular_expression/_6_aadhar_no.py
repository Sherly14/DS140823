# 1st Way

# import re 
# aadhaar_number = input("Enter your aadhaar_number:")
# res = re.findall(r"^[1-9]{1}[0-9]{3}-[0-9]{4}-[0-9]{4}$",aadhaar_number) 
# print(res)
# if res:
#     print(aadhaar_number,"is valid")
# else:
#     print(aadhaar_number, "is not valid")



# 2nd Way
import re 
aadhar_card = input("Enter your aadhar number:")
res = re.findall(r"\b[1-9]{1}[\d]{3}-[\d]{4}-[\d]{4}\b",aadhar_card) 
print(res)
if res:
    print(aadhar_card,"is a valid ")
else:
    print(aadhar_card, "is a invalid ")


# pan_no
# AAAAA1234A