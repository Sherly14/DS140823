# ChainMap
# it is a class from collection module
# used to combine multiple dictionaries together

from collections import ChainMap

dict1 = {"a":"A","b":"B"}
dict2 = {"c":"C","d":"D"}
dict3 = {"e":"E","f":"F"}

obj = ChainMap(dict1,dict2,dict3)
print(obj)

print(obj["e"])

dict4 = {"x":"X","y":"Y"}

obj1 = obj.new_child(dict4)
print(obj1)

obj1.pop("x")
print(obj1)




