lst = [4,5,3,6,8,3,1]

even_lst = []

for i in lst:
    if i % 2 == 0:
        even_lst.append(i)

print(even_lst)

even_lst = [i for i in lst if i % 2 == 0]
print(even_lst)

# str1 = "Python"
# o/p : ["P","y","t","h","o","n"]