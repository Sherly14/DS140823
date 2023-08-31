# 1st Method

# num = int(input("Enter the number :"))

# prime = True

# if num > 1:
#     for i in range(2,num):
#         if num % i == 0:
#             prime = False
#             break

#     if prime == False:
#         print("Given number is not prime.")
#     else:
#         print("Given number is prime.")






# 2nd Method

# num=int(input("enter a number to check prime or not"))

# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")






# 3rd Method

# number = int(input("Enter any number: ")) # 10 - 5
# print(number)
# i=2
# while i<number:
#     if number%i == 0:
#        print("Number is not a prime")
#        break
#     else:
#       print("Number is a prime")
#       break




# 4th Method
num = int(input("Enter a number :"))
for i in range(2,num//2+1):
    if num % i == 0:
        print(num,"is not a prime number")
        break
else:
    print(num,"is a prime number")