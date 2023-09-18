import re

# data = "Hello Vaibhavi"
# res = re.findall("[lbhz]",data)
# print(res)

data = "Hello Vaibhavi"
res = re.findall("[^VBHl]",data) # it will return everything except V,B,H,l
print(res)

data = "Hello Vaibhavi"
res = re.findall("[a-z]{5}",data)
print(res)

data = "67 89"
res = re.findall("[0-7][5-8]",data)
print(res)