# 1st Way

# endvalue= int(input("Enter the total size of the list: "))
# lst =[]
# for i in range(0,endvalue):
#     iptvalue =int(input("Enter the values: "))
#     lst.append(iptvalue)
# print(lst)
# for i in range(len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i]>=lst[j]:
#             lst[i],lst[j]=lst[j],lst[i]

# print(lst)
# print("largest value",lst[-1])






# 2nd Way
# size = int(input("Enter total elements to be in the list:"))
# lst = []
# for i in range(0,size):     
#     print("Enter",i+1, "element:")
#     elements = input()
#     lst.append(elements)
# print(lst)

# largest_num = lst[0] # 5
# for num in lst:
#     if num > largest_num: # 3 > 6
#         largest_num = num # 6

# print(largest_num, "is the largest number in the list")





# 3rd Way

# size = int(input("Enter the size of the list: "))
# largest_value = None
# for i in range(size):
#     n = float(input("Enter the value: "))
#     if largest_value is None or n > largest_value:
#         largest_value = n

# if largest_value is not None:
#     print("The largest value in the list is:",largest_value)
# else:
#     print("No values were entered, so there is no largest value.")



# 4th Way

# size = int(input("Enter the size : "))
# lst = []

# for i  in range(0,size):
#     element = int(input("Enter the elements : "))
#     lst.append(element)
# print(lst)
# lst1 = lst
# lst1.sort()
# print(lst1[-1])





# 5th Way
my_list = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    element = int(input("Enter element {}: ".format(i + 1)))
    my_list.append(element)
largest_value = max(my_list)
print("The largest value in the list is:", largest_value)


# dynamic list
# reverse it

[6,7,4,1,10]
[10,1,4,7,6]