# 1st Way 
# import re 
# pan_card = input("Enter your aadhar number:")
# res = re.findall(r"\b[A-Z]{5}\d{4}[A-Z]{1}\B",pan_card) 
# print(res)
# if res:
#     print(pan_card,"is a valid ")
# else:
#     print(pan_card, "is a invalid ")


# 2nd Way
# import re
# data=input("enter the pan number:")
# res = re.findall(r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$",data)#AAAAA1234N
# print(res)
# if res:
#     print(data,"is valid")
# else:
#     print(data,"is not valid")


# email_id
# characters,dot,underscore,digits@small_characters.small_characters