import re

# data = "Hello Students!"
# res = re.findall(r"\AHello",data) # starts with Hello
# print(res)

# data = "Hello Students!"
# res = re.findall(r"Students!\Z",data) # ends with Stduents!
# print(res)

# data = "Hello Students! Hell ya!"
# res = re.findall(r"\bHell",data) # checks for all the words which starts with "Hell"
# print(res)

# data = "Hello Students! Hell ya!"
# res = re.findall(r"\Ba",data) # checks for all the words which ends with 'a'
# print(res)

# data = "Hello Students! Hell ya! 123"
# res = re.findall(r"\d",data) 
# print(res)

# data = "Hello Students! Hell ya! 123"
# res = re.findall(r"\D",data) 
# print(res)

# data = "Hello Students! Hell ya! 123"
# res = re.findall(r"\s",data) 
# print(res)

# data = "Hello Students! Hell ya! 123"
# res = re.findall(r"\S",data) 
# print(res)

data = "Hello Students! Hell ya! 123 _ _ _ _ _ _"
res = re.findall(r"\w",data)  # if checks if A-Z,a-z,0-9,_
print(res)

data = "Hello Students! Hell ya! 123 _ _ _ _ _ _"
res = re.findall(r"\W",data)  # if checks everything except A-Z,a-z,0-9,_
print(res)