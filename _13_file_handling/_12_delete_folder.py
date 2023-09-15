# provide path in file
import os

file = r"C:\Users\vashi\OneDrive\Documents\GitHub\DS140823\test_folder"
file_names = os.listdir(file)
print(file_names)
for i in file_names:
    os.remove(f"{file}\{i}")
os.rmdir(file)


# create a new file (a.txt)
# write some data in it
# fetch that written data from that file (a.txt)
# store it inside a new file (b.txt)