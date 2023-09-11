# function without parameter and without return statement

# def addition():  
#     no1 = int(input("Enter no1 : "))
#     no2 = int(input("Enter no2 : "))
#     add = no1 + no2
#     print("Addition : ",add)

# addition()






# function without parameter and with return statement

# def addition():  
#     no1 = int(input("Enter no1 : "))
#     no2 = int(input("Enter no2 : "))
#     add = no1 + no2
#     return add

# result = addition()
# print("Result : ",result*10)







# function with parameter and without return statement

# def addition(num1,num2):  # parameter / argument 
#     # no1 = int(input("Enter no1 : "))
#     # no2 = int(input("Enter no2 : "))
#     add = num1 + num2
#     print("Addition : ",add)

# addition(6,7)





# function with parameter and with return statement

def addition(num1,num2):  # parameter / argument 
    add = num1 + num2
    print("Addition : ",add)
    return add

no1 = int(input("Enter no1 : "))
no2 = int(input("Enter no2 : "))
res = addition(no1,no2)
print(res)

