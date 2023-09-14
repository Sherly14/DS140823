# seek function
# it allows you to modify the cursor position

# seek(offset,from_what)
# offset - no of position to move forward
# from_what - point of reference

# from_what - bydefault value  - 0
# 0 - beginning         - text file
# 1 - current position
# 2 - end of the file

file = open("demo.txt","w")

cur_pos = file.tell()
print("Cursor Position : ",cur_pos)

file.seek(4,0)

cur_pos = file.tell()
print("Cursor Position : ",cur_pos)
