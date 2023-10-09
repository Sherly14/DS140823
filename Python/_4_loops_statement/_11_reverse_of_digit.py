num = int(input("Enter number:")) # 123 = 321

reverse = 0

while num != 0 :                           # 123 != 0 # 12 != 0          # 1 != 0  # 0 != 0
    digit = num % 10                       # 3        # 2                # 1
    reverse = (reverse*10) + digit         # 3        # 3 * 10 + 2 = 32  # 32 * 10 + 1 = 321
    num =  num // 10                       # 12       # 1                # 0 
print(reverse) 