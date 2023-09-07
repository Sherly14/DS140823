# size=int(input("enter your list size:"))
# list1=[]
# for i in range(size):
#     print("enter your ",i," element:",end="")
#     list1.append(int(input()))

# print(list1[::-1])




# size =int(input("enter the size of list : "))
# lst = []
# for i in range(size):
#   elements = input("enter the elements:")
#   lst.append(elements)
#   print(lst)
# lst.reverse()
# print(lst)





# num_size = int(input("Enter total elements for list : "))
# lst = list()
# for i in range(num_size):
#     elements = input("Enter elements:")
#     lst.append(elements)
# print("Original List : ", lst)

# revlist = list()
# for i in range(num_size-1, -1, -1):
#     revlist.append(lst[i])

# print("Reversed List : ", revlist)






size = int(input("Enter the size of the list: ")) # 5
lst = []
for i in range(size):
    n = input("Enter value : ")
    lst.append(n)

print("og : ",lst)
left = 0                 #  7
right = size - 1 # 4     #  9

while left < right:
    lst[left], lst[right] = lst[right], lst[left]
    left += 1 
    right -= 1 

    print(lst)

print("Reversed list:")
for value in lst:
    print(value)



# size=int(input())
# lst=[]
# for i in range(size):
# 	num=int(input())
# 	lst.append(num)
# print(lst)

# lst2=[]
# for i in range(1,len(lst)+1):
# 	lst2.append(lst[-i])
# print(lst2)