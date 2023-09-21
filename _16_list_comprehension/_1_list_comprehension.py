# list comprehension - it is use to create one list from another in minimal code

# for i in lst:
#     if <condition>:
#         body

# [body for i in lst if <condition>]

nums = [5,6,3,2,6,7,9,10]

new_lst = []
for i in nums:
    new_lst.append(i)
print(new_lst)

new_lst = [i for i in nums]
print(new_lst)
