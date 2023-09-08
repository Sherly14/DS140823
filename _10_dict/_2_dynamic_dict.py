my_dict = {}

num_pairs = int(input("Enter the number of key-value pairs: "))

for i in range(num_pairs):
    key = input("Enter key: ")
    value = input("Enter value: ")
    my_dict[key] = value
    
print("Dictionary created:", my_dict)