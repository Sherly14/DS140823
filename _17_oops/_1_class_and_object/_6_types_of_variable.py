# local variable
# global variable
# instance variable

# class/static variable
# it's defined inside the class but outside the method/constructor
# scope is throughout the class
# class variable can be accessed using class name <class_name>.<class_variable>, but it can also be called using object
# it is use for memory management
# as it shares the same memory



class school:

    school_name = "Coder"               # class/static variable

    def __init__(self,rno,name):
        self.name = name
        self.rno = rno

    def display(self):
        print(f"Rno : {self.rno} || Name : {self.name} || School Name : {school.school_name}")

obj = school(1,"Vinu")
obj.display()

obj1 = school(2, "Vaibhavi")
obj1.display()        

obj2 = school(3, "Vinay")
obj2.display() 