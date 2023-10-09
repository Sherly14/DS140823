file1 = open("original.txt", "w+")
file1.write("My Name is Vinuthna")
file1.seek(0,0)
data = file1.read()
file1.close()

file3 = open("new_file.txt", "w")
file3.write(data)
file3.close()