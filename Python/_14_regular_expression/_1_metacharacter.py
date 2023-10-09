import re 

# data = "Hello"
# res = re.findall("[a-z]",data)
# print(res)

# data = "Hello123"
# res = re.findall("[A-Z]",data)
# print(res)

# data = "Hello123"
# res = re.findall("[A-z]",data)
# print(res)

# data = "Hello123"
# res = re.findall("[a-zA-Z]",data)
# print(res)

# data = "Hello123"
# res = re.findall("[d-h]",data)
# print(res)

# data = "HELLO123"
# res = re.findall("[D-H]",data)
# print(res)

# data = "Hello123"
# res = re.findall("\d",data)
# print(res)

# data = "Hello 123?"
# res = re.findall("\D",data)
# print(res)

# data = "Python is a programming language"
# res = re.findall("is",data)
# print(res)

# data = "Python is a programming language"
# res = re.findall("is|language|Bharati",data)
# print(res)

# data = "Hello Students!"
# res = re.findall("H...o",data)
# print(res)

# data = "Hello Students!"
# res = re.findall("H.*o",data) # 0 or more between H and o
# print(res)

# data = "Helloooooooo Students!"
# res = re.findall("H.+o",data) # 1 or more between H and o
# print(res)

# data = "Hello Students!"
# res = re.findall("H.?o",data) # 0 or 1 between H and o
# print(res)

# data = "Hellooo Students!"
# res = re.findall("H.{5}o",data) # 5 between H and o
# print(res)

data = "Hello Students!"
res = re.findall("^Hel",data)
print(res)

data = "Hello Students!"
res = re.findall("s!$",data)
print(res)