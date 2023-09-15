import os

# delete the file
# os.remove("testfile.txt")

# os.remove("C:\\Users\\vashi\\OneDrive\\Documents\\testing.txt")

# checks if file already exist or not
# is_exists = os.path.exists("test.txt")
# print("Is exist : ",is_exists)

# data = os.listdir(r"C:\Users\vashi\OneDrive\Documents\GitHub\DS140823\test_folder")
# print(data)


# delete the directory
# os.rmdir(r"C:\Users\vashi\OneDrive\Documents\GitHub\DS140823\test_folder")


# x mode
# creates the file but if already exist then it will raise an error
file = open("abc.txt","x")
file.write("hello")





