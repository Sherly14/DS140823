# # int
# immutable
# num = 2 
# print("Int : ",2)

# # # float
# immutable
# salary = 10000.34
# print("Float : ",salary)

# # # str
# immutable
# name = "Bharati"
# print("Str : ",name)

# # # bool
# immutable
# night = True
# print("Bool : ",night)

# # # complex
# immutable
# comp = 2+9j
# print("Complex : ",comp)




# # # Collections
# # list
# are used to store more than one value
# [] / list()
# indexed-based (starts with 0)
# it allows you to store heterogenous data (values of different datatype)
# duplicates are allowed
# mutable (modifiable)
# ordered - it considers the same order in which you inserted  the value in list

# lst = [2,5,6,78,2,0,"Bharati",9.8,True]
# print(lst)

# print(lst[7])
# print(lst[3])

# lst[6] = "Vivek"
# print(lst)

# lst1 = list([2,5,6,78,2,0,"Bharati",9.8,True])
# print(lst1)

# data_type = type(lst)
# data_type1 = type(lst1)
# print(data_type)
# print(data_type1)




# tuple
# are used to store more than one value
# () / tuple()
# accepts heterogenous data
# accepts duplicate
# indexed-based
# immutable (cannot modify)

# tup = (5,3,7,2,1,4,6,8,10,"Bharati",True,10)
# print(tup)

# print(tup[8])

# tup1 = tuple([1,2,3,4,5,6])
# print(tup1)

# data_type = type(tup)
# data_type1 = type(tup1)
# print(data_type)
# print(data_type1)

# tup[2] = 70 # cannot modify



# set
# are used to store more than one value
# {} / set()
# accepts heterogenous data
# unordered
# non-indexed
# duplicates are not allowed
# mutable

# set_demo = {6,7,3,1,2,89,100,"Bharati",6,True}
# print(set_demo)

# set_demo.add(67)
# print(set_demo)

# # print(set_demo[0])

# set_demo1 = set([1,2,6,7,4,3])
# print(set_demo1)

# data_type = type(set_demo)
# data_type1 = type(set_demo1)
# print(data_type)
# print(data_type1)



# dict (dictionary)
# {} / dict()
# {key-value} - item
# non-indexed
# key - duplicate values are not allowed
# value - duplicates are allowed
# unordered (when huge data)
# accepts heterogenous data
# mutable

dict_demo = {'a':"Bharati",'b':"Vaibhavi","c":"Ankit",4:"Bharati"}
print(dict_demo)

print(dict_demo["b"])

dict_demo["c"] = "Vivek"
print(dict_demo)











