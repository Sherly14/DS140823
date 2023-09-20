# Lambda Function

# it is an anonymous(unnamed) function
# it s a function without a name
# it can have any no. of parameters but only one expression(condition) allowed
# it doesn't have return statement
# it helps to create one liner function


def add(a,b):
    return a+b

res = add(7,8)
print(res)


res = lambda a,b : a+b 
print(res(7,8))