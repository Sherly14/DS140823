div = 0
no1 = int(input("Enter no1 : "))
no2 = int(input("Enter no2 : "))
try:
    div = no1 / no2
except :
    print("don't enter zero in Denominator ")
    no2 = int(input("Enter no2 : "))
    div=no1/no2

print("Division : ",div)
print("End of program")

# # try : is use to hold suspicous code
# # except : is use to hold handling code for the code mentioned in try block

