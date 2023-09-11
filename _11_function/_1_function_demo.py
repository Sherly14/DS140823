# Function 

# set of code which can be re-used
# to develop clean and maintainable code
# optimize the code

# syntax :
# def <function_name>():
#     body

# def addition():   # defining the function
#     no1 = int(input("Enter no1 : "))
#     no2 = int(input("Enter no2 : "))
#     add = no1 + no2
#     print("Addition : ",add)

# addition() # calling the function
# addition()
# addition()


def prime_no():
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


prime_no()