# 1. local variable
# - are variables which are define inside the function
# - scope - within the function itself

# 2. global variable
# - are variables which are define outside the function
# - scope - throughout the python file

name = "Bharati"

def add():
    no1 = 10           # local variable
    no2 = 90           # local variable
    add = no1 + no2    # local variable
    print(add)
    print(no1)
    print("inside function : ",name)
    global address
    address = "Mumbai"
    print(address)

add()

print("outside function : ",name)
print(address)

