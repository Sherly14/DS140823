# size_of_lst = int(input("Enter the size of list:"))
# lst = []
# for i in range(size_of_lst):
#     elements = input(f"Enter the {i} element :")
#     lst.append(elements)
# print(lst)

# def reverse():
#     return lst[::-1]
# print(reverse())




def reverse(list1):
    last=len(list1)-1
    for i in range(len(list1)//2):
        temp=list1[i]
        list1[i]=list1[last]
        list1[last]=temp
        last-=1
        
size=int(input("enter your list size:"))
list1=[]
for i in range(size):
    print("enter your",i,"element: ",end="")
    list1.append(int(input()))
    
reverse(list1)
print(list1)



str1 = arti 
str2 = tiar

str2 is rotation of str1
arti

tiar