# class methods are use to modify class/static variable

class school:

    school_name = "Coder"               # class/static variable

    def __init__(self,rno,name):
        self.name = name
        self.rno = rno

    def display(self):
        print(f"Rno : {self.rno} || Name : {self.name} || School Name : {school.school_name}")

    @classmethod                       # decorator
    def get_school_name(cls):          # class method
        return cls.school_name

    @classmethod
    def set_school_name(cls,sname):
        cls.school_name = sname

obj = school(1,"Vinu")
obj.display()

obj1 = school(2, "Vaibhavi")
obj1.display()        

obj2 = school(3, "Vinay")
obj2.display() 

data = school.get_school_name()
print(data)

school.set_school_name("Edyoda")

data = school.get_school_name()
print(data)

obj2.display() 