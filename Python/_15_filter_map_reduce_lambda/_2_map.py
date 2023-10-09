lst = [4,5,57,6,3,2,43,5]

# def square(lst):
#     lst_squ = []
#     for i in lst:
#         lst_squ.append(i**2)
#     return lst_squ

# res = square(lst)
# print(res)

def square(lst):
    return lst ** 2

res = list(map(square,lst))
print(res)