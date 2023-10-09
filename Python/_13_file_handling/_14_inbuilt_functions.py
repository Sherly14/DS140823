file = open("demo.txt","w")

# data = file.read() # reads the whole data
# print(data)


# data = file.read(5) # reads only 5 characters
# print(data)


# data = file.readline() # reads the first line
# print(data)


# data = file.readlines()
# print(data)


# for i in file:
#     print(i)


# file.write("Hello")

lst = ["Hey\n","Byeee\n","Good Morning\n","Good Night"]
file.writelines(lst)