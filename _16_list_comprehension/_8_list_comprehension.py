lst1 = [1,2,3,4,5]
lst2 = [4,5,6,7,8]

lst = []
for i in lst1:
    for j in lst2:
        if i == j:
            lst.append(i)
print(lst)

lst = [i for i in lst1 for j in lst2 if i == j]
print(lst)



lst = [6,7,2,3,9,9,1,8,3] # 0,2,5,7
o/p : [6,2,9,8]