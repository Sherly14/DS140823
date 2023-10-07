# Counter

# it is a class from collection module
# it is a child class of dict class
# it will consider the elements as keys and the count of elements as values

# ["a","a","b","a","c","c"]
# {a : 3,b : 1,c: 2}

from collections import Counter

lst = ["a","a","b","a","c","c"]
counter = Counter(lst)
print(counter)

counter1 = Counter(a=4,b=9,c=10)
print(counter1)