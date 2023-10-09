# * * * *
# *     *
# *     *
# * * * *

for i in range(1,5):
     for j in range(1,5):
        if j == 1 or i == 1 or i == 4 or j == 4:
           print("*",end=" ")
        else:
           print(" ",end=" ")
     print()    




