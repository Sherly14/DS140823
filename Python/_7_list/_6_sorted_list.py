# 1st Way

# num = int(input("enter number of elements required: "))
# lst = []
# for i in range(num):
#     element = int(input())
#     lst.append(element)
# print("Original List:", lst)
 
# # [3, 2, 1]
# for i in range(len(lst)):                   # i = 3
#     for j in range(i+1,len(lst)):           # j = 3
#         if lst[i] >= lst[j]:                # 3 > 2      # 2 > 1   # 3 > 2
#             lst[i], lst[j] = lst[j],lst[i]  # [2,3,1] |  [1,3,2]   | [1,2,3]
#             print(lst)

# print("Sorted List", lst)








# 2nd Way
# size = int(input("Enter the size of the list: "))
# lst= []
# for i in range(size):
#     elements_ = int(input("Enter :"))
#     lst.append(elements_)
# print(lst)

# for i in range(size):
#      for j in range(i+1,size):
#           if (lst[i] >= lst[j]):
#                temp = lst[i]
#                lst[i] = lst[j]
#                lst[j] = temp
#                print(lst)
# print("Sorted list : ", lst)


# [7,8,3,7,4,3,10,9]
# [7,8,3,4,10,9]  - set()
# [8,4,10,9]      - expected o/p
