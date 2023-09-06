num = int(input("enter number of elements required: "))
lst = []
for i in range(num):
    element = int(input())
    lst.append(element)
print("Original List:", lst)
 
# [3, 2, 1]
for i in range(len(lst)):      # i = 0 - 3
    for j in range(i+1,len(lst)): # j = 3        - 1
        if lst[i] >= lst[j]: # 3 >= 1
            lst[i], lst[j] = lst[j],lst[i] # [2,3,1] | [2,1,3]
            print(lst)
        print(lst)

print("Sorted List", lst)


