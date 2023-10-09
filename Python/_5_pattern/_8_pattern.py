# *     *
#      
#      
# *     *


# 11 12 13 14
# 21 22 23 24 
# 31 32 33 34 
# 41 42 43 44 


for i in range(1, 5):
    for j in range(1, 5):
        # if (i == 1 and j == 1) or (i == 1 and j == 4) or (i == 4 and j == 1) or (i == 4 and j == 4):
        # if (i == 1 and ( j == 1 or j == 4)) or (i == 4 and (j == 1 or j == 4)):
        if (i, j) in [(1, 1), (1, 4), (4, 1), (4, 4)]:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


