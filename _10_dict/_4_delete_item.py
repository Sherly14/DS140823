# 1st Way
# my_dict = {}

# num_pairs = int(input("Enter the number of key-value pairs: "))

# for i in range(num_pairs):
#     key = input("Enter key: ")
#     value = float(input("Enter value: "))
#     my_dict[key] = value
# print(my_dict)

# new_key=input("enter the new key:")
# my_dict.pop(new_key)
# print(my_dict)




# 2nd Way
# size=int(input("enter dict size:"))
# dict1={}
# for i in range(size):
#     print("enter  key:",end="")
#     key1=input()
#     print("enter your value:",end="")
#     value1=int(input())
#     dict1[key1]=value1
# print(dict1)

# value2=input("enter your value to check:")
# if value2 in dict1:
#    for i in dict1:
#        if i==value2:
#            dict1.pop(i)
#            break
# else:
#     print("value is not in dict1")
       
# print(dict1)  





# 3rd Way
# size=int(input("Please enter the size of dictionary"))
# dict={}
# for i in range(size):
# 	key=input("Enter a key element")
# 	val=int(input("Enter a value"))
# 	dict[key]=val
# print(dict)
# val1=input("please enter the key name to delet the element")
# dict2={}
# for i in dict:
# 	for j in dict.values():
# 		if i!=val1 and j!=dict[i]:
# 			dict2[i]=j
# print(dict2)




# 4th Way
# num_size = int(input("Enter the size of the dictionary : "))
# my_dict = {}
# for i in range(num_size):
#     key = input("\nEnter the key : ")
#     value = int(input("Enter the value : "))
#     my_dict[key] = value
# print("\nMy Dictionary : ",my_dict)

# key_del = input("Enter the key which you want to delete from dictionary : ")

# for i in my_dict.keys():
# 	if i == key_del:
# 		del my_dict[i]
# 		break
# print(my_dict)





# 5th Way
# size=int(input("Please enter the size of dictionary"))
# dict={}
# for i in range(size):
# 	key=input("Enter a key element")
# 	val=int(input("Enter a value"))
# 	dict[key]=val
# print(dict)
# val1=input("please enter the key name to delet the element")

# for i,j in dict.items():
# 	if i == val1:
# 		del dict[i]
# 		break
# print(dict)




# 6th Way
size = int(input("Enter the number of dictionary: "))
my_dict = {}
for _ in range(size):
    key = input("Enter a key: ")
    value = input("Enter a value: ")
    my_dict[key] = value

key_to_delete = input("Enter a key to delete: ")
keys_to_delete = [key for key, val in my_dict.items() if key == key_to_delete]
if keys_to_delete:
    my_dict = {key: val for key, val in my_dict.items() if key not in keys_to_delete}
    print("Updated dictionary:")
else:
    print("No key with value found in the dictionary. Dictionary remains unchanged.")
for key, value in my_dict.items():
    print(f"{key}: {value}")