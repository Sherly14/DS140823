# 1st Way 

# import re 
# mobile_number = input("Enter your mobile_number:")
# res = re.findall(r"^[+91]{3}[ ]{1}[6-9]{1}[0-9]{9}$",mobile_number) 
# print(res)
# if res:
#     print(mobile_number,"is a valid mobile number")
# else:
#     print(mobile_number, "is a invalid mobile number")




# 2nd Way 

# import re

# def validate_mobile_number(number):
#     pattern = re.findall(r'^\+91 [6-9]\d{9}$',number)
#     return pattern

# mobile_number = input("Enter the mobile number :")
# pattern2=validate_mobile_number(mobile_number)
# if len(pattern2)!=0:
#     print(pattern2," valid mobile number")
# else:
#     print(pattern2,": invalid mobile number")



# 3rd Way 

# import re

# data = input("enter your mobile number: ")
# res = re.findall(r"^[+91 ]{4}[6-9]{1}[0-9]{9}$",data)
# print(res)
# if res:
#     print("Format is correct")
# else:
#     print("Format is incorrect")


# aadhar_no

# # 12 digits, no character
# # should not start with 0
# # 1234-4567-7890

