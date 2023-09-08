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
print("OG : ",dict_demo)

# dict_demo["z"] = "Mamatha"
# print("Add : ",dict_demo)

# dict_demo["b"] = "Pranay"
# print("Update : ",dict_demo)

dict_demo.update({"b":"Pranay"})
print("Update : ",dict_demo)

# dict_demo.pop("a")
# print(dict_demo)

# keys = dict_demo.keys()
# print(keys)

# values = dict_demo.values()
# print(values)

# items = dict_demo.items()
# print(items)

# for k,v in dict_demo.items():
#     print(k,"---->",v)

# for k in dict_demo.keys():
#     print(k)

# for v in dict_demo.values():
#     print(v)


# # data = dict_demo["b"]
# # print(data)

# # data = dict_demo.get("r",False)
# # print(data)

# dict1 = dict_demo.copy()
# print("Copy : ",dict1)

# dict_demo.clear()
# print("Clear : ",dict_demo)


# size
# input
# dict