# instance variable
# define inside the method/constructor with 'self' as prefix
# scope - throughout the class


class student:

    def __init__(self,rno,name):
        self.rno = rno 
        self.name = name

    def display(self):
        print(f"Rno : {self.rno} and Name : {self.name}")

student_obj = student(10,"Bijo")
student_obj.display()

