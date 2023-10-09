import memory_profiler as memory

# def fun(no):
#     lst = []
#     for i in range(no):
#         lst.append(i)
#     return lst

# print("Before calling function : ",memory.memory_usage())
# fun(10000000)
# print("After calling function : ",memory.memory_usage())

# Before calling function :  [19.31640625]
# After calling function :  [20.1953125]



def gen(no):
    for i in range(no):
        yield i

print("Before calling function : ",memory.memory_usage())
gen(10000000)
print("After calling function : ",memory.memory_usage())


# Before calling function :  [19.37109375]
# After calling function :  [19.37890625]