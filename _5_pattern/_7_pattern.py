#     *
#     *
# * * * * * 
#     *
#     *

# 11 12 13 14 15
# 21 22 23 24 25
# 31 32 33 34 35
# 41 42 43 44 45
# 51 52 53 54 55

for i in range(1,6):
    for j in range(1,6):
        if i==3 or j==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# *     *
#      
#      
# *     *