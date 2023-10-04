import pdb

def addition(no1,no2):
    add = no1 + no2
    return add

pdb.set_trace()
no1 = input("Enter no1 : ")
no2 = input("Enter no2 : ")
data = addition(no1,no2)
print(data)