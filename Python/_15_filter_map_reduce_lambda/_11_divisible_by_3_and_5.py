lst = [5,61,90,34,55,100,95,15,30]
lst1 = list(filter(lambda lst : lst % 3 ==0 and lst % 5 == 0,lst))
print(lst1)