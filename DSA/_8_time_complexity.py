# Time Complexity

# time taken by program to give the response

lst = [6,4,1,5,89,12,3,45,67,12,3]
# Best Case = lst[0]               # 1 iteration
# Worst Case = lst[10] / lst[-1]   # 11 iterations
# Average Case = lst[5]            # 6 iterations

# Time Complexities : 

# 1. Constant Time O(1)

# print("Hello")

# a = 10
# b = 20

# def time():
#     if a > b:
#         return True
#     else:
#         return False
# time()






# 2. Linear Time : O(n)

n = 11000
for i in range(n):
    print(i)






# 3. Quadratic Time : O(n^2)

for x in range(n):
    for y in range(n):
        print(x,y)




# 4. Exponential Time : O(2^n)
# 
# Recurrsion 