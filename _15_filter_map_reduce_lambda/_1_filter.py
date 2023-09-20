lst = [4,5,57,6,3,2,43,5]

# def get_even(lst):
#     lst_even = []
#     for i in lst:
#         if i%2 == 0:
#             lst_even.append(i)
#     return lst_even

# even = get_even(lst)
# print(even)



# def get_even(lst):
#     return lst % 2 == 0

# even = list(filter(get_even,lst))
# print(even)



even = list(filter(lambda lst : lst % 2 == 0,lst))
print(even)