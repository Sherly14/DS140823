# num = int(input("Enter the number to find factorial:"))
# factorial = 1
# for i in range(1,num+1):
#     factorial *= i
# print(factorial)


num = int(input("Enter the num: "))
fact = 1
for i in range(1,num+1):
    fact = i * fact
    print(fact)
print(fact)