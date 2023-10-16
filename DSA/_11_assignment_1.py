# size = int(input("Enter no of ele  in list :"))
# list_num = []
# for i in range(size):
#     ele = int(input(f"Enetr the {i} element : "))
#     list_num.append(ele)
# print(list_num)

# num = int(input("Enetr the sum you want : "))

# def  find_pairs(lst, num):
#     pairList = []
#     for i  in lst:
#         for j in lst:
#             if i+j == num:
#                 pairList.append([i,j]) 
#     return pairList

# print(find_pairs(list_num, num))




def pairs(list1,find):
    list2=[]
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if list1[i]+list1[j]==find:
                touple1=(list1[i],list1[j])
                list2.append(touple1)
    return list2
        

size=int(input("enter your list size:"))
list1=[]
for i in range(size):
    print("enter your",i,"element: ",end="")
    list1.append(int(input()))
find=int(input("enter your element :"))
print(pairs(list1,find))
