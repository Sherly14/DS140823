name = input("Enter your name : ")
age = int(input("Enter your age : "))

if age >= 18:
    qualification = int(input("Enter your qualification in number : "))
    if qualification >= 15:
        print("You are hired!!!")
    else:
        print("We need more qualified candidate")
else:
    print("Mandatory age should be 18 or above!")