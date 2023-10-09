# Slicing Operator [:]
# it is use to fetch the substring of a string

str1 = "Python is a programming language"

res = str1[7:17] # start_index, end_index
print(res)

res = str1[7:14] # start_index, end_index
print(res)

res = str1[2:]
print(res)

res = str1[:7]
print(res)

res = str1[:]
print(res)

res = str1[-1:]
print(res)

res = str1[-8:-4]
print(res)

res = str1[1:6:2] # 1,3,5
print(res)

res = str1[::-1]
print(res)

for i in range(10,0,-1):
    print(i)

