# Generator

# generators are functions
# it is memory efficient
# it does not allocate memory to all the objects at the sametime
# it allocates the memory to the object when it is demanded

# Two ways of creating generators 

# 1st Way : 

# def fun(no):
#     yield no*2

# data = fun(10)
# print(data)
# print(next(data))








# 2nd Way :

gen = (i*2 for i in range(1,11)) # 2,4,6,8,10,12,14,16,18,20
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))