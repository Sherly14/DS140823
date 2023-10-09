number=int(input("enter int value"))

copynum=number
count=-1
while number!=0:
    count+=1
    number//=10
number=copynum
newnum=0
while number!=0:
    digit=number%10
    number//=10
    newnum += digit*(10**count)
    print("newnum : ",newnum)
    count-=1
    
if newnum==copynum:
    print(f"the number {newnum} is palindrome")
else:
    print(f"the number {newnum} is not palindrome")