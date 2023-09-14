file = open("test.txt")
# file.close()

mode = file.mode
print('Mode : ',mode)

file_name = file.name
print("File Name : ",file_name)

is_close  = file.closed
print("Close : ",is_close)
