size = int(input("Enter total elements to be in the list:"))
lst = []
for i in range(0,size):     
    print("Enter",i+1, "element:")
    elements = input()
    lst.append(elements)
print(lst)

unique_list = []
for item in lst:
    if lst.count(item) == 1:
        unique_list.append(item)
print("The unique elements from the given list", lst , "is:",unique_list)


# dynamic list
# largest value

# [6,8,3,1,8,1,45,10]
# 45