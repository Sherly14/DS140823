no1 = int(input("enter number 1: "))
no2 = int(input("enter number 2: "))
no3 = int(input("enter number 3: "))

if no1 > no2 and no1 > no3:
    print("no1 is max")
elif no2 > no1 and no2 > no3:
    print("no2 is max")
elif no1 == no2 == no3 :
    print("All are equal")
else:
    print("no3 is max")