rows = int(input("Enter number of rows:"))   # 3      
col  = int(input("Enter number of column:")) # 2

matrix = []

for i in range(1,rows+1):
    row = []
    for j in range(1,col+1):
        element = input(f"Enter element in {i}{j}:")
        row.append(element)
    matrix.append(row)

print("Matrix:")
for row in matrix:
    print(row)