num = int(input("Enter number:")) # 564 = 5 + 6 + 4 = 15
sum = 0

while num > 0 :        # 564 > 0 || 56 > 0 || 5 > 0 || 0 > 0
    digit = num % 10   # 4       || 6      || 5
    sum = sum + digit  # 4       || 10     || 15
    num =  num // 10   # 56      || 5      || 0
print(sum) 

# int value from user 
# 754 - 457