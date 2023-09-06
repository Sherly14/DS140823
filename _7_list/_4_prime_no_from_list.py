total =int(input("enter total numbers")) # 5

numbers=[]
for i in range(total): # i = 5
    element = int(input('enter value'))
    numbers.append(element)

print(numbers)

primelst=[]
for num in numbers: 
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                break
        else:
            primelst.append(num)
            
print(primelst)

# size
# input and create list
# ask for a input
# whether that input is present inside the list or not 