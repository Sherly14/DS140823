# set comprehension - it is use to create a set from list,tuple,set

lst = [45,6,3,2,57,3]

even = {i for i in lst if i % 2 == 0}
print(even)
