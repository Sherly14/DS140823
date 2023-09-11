# 1st Way
# size = int(input("Enter total elements to be in the dict:"))
# print()
# dict = {}
# for i in range(size):     
#     print("Enter",i+1, "key:")
#     key = input()
#     print("Enter",i+1, "value:")
#     value = int(input())
#     print()
#     dict[key] = value
# print("The dictionary is:", dict)

# sum = 0
# for value in dict.values():
#     sum += value
# print("Sum of values in dict:",sum)




# 2nd Way
my_dict = {}
n = int(input("Enter the number of key-value pairs: "))

for i in range(n):
    key = input(f"Enter key {i + 1}: ")
    value = float(input(f"Enter value for {key}: "))
    my_dict[key] = value

total_sum = sum(my_dict.values())
print("Sum of all values:", total_sum)


# ask value
# check if it matches with any key
# if yes then that item should be deleted