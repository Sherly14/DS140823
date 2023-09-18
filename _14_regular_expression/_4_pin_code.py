import re

pin_code = input("Enter your pincode : ")

res = re.findall(r"^[1-9][0-9]{5}$",pin_code)

print(res)

if res:
    print("Format is correct")
else:
    print("Format is incorrect")

# mobile number
# only digit
# only 10 digit
# shouldn't start with 0