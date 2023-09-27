# Polymorphism
# many form

# single entity many forms

# Types of Polymorhphism
# 1. Compile-time polymorphism - overloading - this is not supported in python
# 2. Runtime polymorphism      - overriding

# 1. Compile-time polymorphism
# class Shape:
#     def area(self,radius):
#         return 3.14*radius*radius
    
#     def area(self,length,breadth):
#         return length * breadth
    
# shape = Shape()
# shape.area(8)


# 2. Runtime polymorphism
class Dad:                          
    def bike(self):
        print("Old Bike")

class Son(Dad):                     
    def bike(self):
        print("Modified Bike")

son = Son()
son.bike()


# Rules of Runtime Polymorphism
# 1. Inheritance is required
# 2. when overriding then method name should be same
# 3. when overriding then method number of parameters should be same