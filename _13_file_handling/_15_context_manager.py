# Context Manager 

# it automatically closes the file, no need to do it manually

with open("demo.txt","w") as file: # file = open("demo.txt","w")
    file.write("Hey")
    file.close() # not required

is_closed = file.closed
print(is_closed)