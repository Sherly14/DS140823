# * 
#   *
#     * 
#       * 


for i in range(1,5):    # i = 1    # rows
    for j in range(1,5):  # j = 4   # cols 
        if i == j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() 