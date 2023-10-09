# Dunder Method | Special Method | Magic Method

# print(dir(list))

# __init__
# __str__
# __mro__


# no1 = 10
# no2 = 20
# add = no1 + no2 # __add__ - dunder method
# print(add)

class special:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def __add__(self,self1):              # here I am overriding Guido's __add__ dunder method
        return self.salary + self1.salary # it's using original __add__ dunder method 
    
    def __mul__(self,self1):
        return self.salary * self1.salary
    
    def __len__(self):
        return len(self.name)

    
obj1 = special("Raj",10000)
obj2 = special("Ram",20000)

print(obj1 + obj2) # it's using my modified __add__ dunder method

print(obj1 * obj2)

print(len(obj1))

        