div = 0
no1 = int(input("Enter no1 : "))
no2 = int(input("Enter no2 : "))
try:
    div = no1 / no2
except (ZeroDivisionError,TypeError) as ex:
    print(ex)
    

print("Division : ",div)
print("End of program")


