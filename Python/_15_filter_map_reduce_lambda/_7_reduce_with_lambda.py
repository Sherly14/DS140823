from functools import reduce

lst = [4,5,3,2,5]

# def total(lst):
# 	sum=0
# 	for i in lst:
# 		sum+=i
# 	return sum

# sum_value = total(lst)
# print(sum_value)



# def total(lst1,lst2):
# 	return lst1 + lst2

# sum_value = reduce(total,lst)
# print(sum_value)



sum = reduce (lambda lst,lst1: lst + lst1 ,lst)
print(sum)