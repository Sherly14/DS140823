import string

def contains_all_alphabet_letters(input_str):
    input_set = set(input_str.lower())
    alphabet_set = set(string.ascii_lowercase)
    print(string.ascii_lowercase)
    
    return alphabet_set <= input_set

value = input("Enter a string: ")
result = contains_all_alphabet_letters(value)
if result:
    print("The string contains all letters of the alphabet.")
else:
    print("The string does not contain all letters of the alphabet.")


