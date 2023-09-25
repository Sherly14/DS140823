# instance variable
# define inside the method/constructor with 'self' as prefix
# scope - throughout the class


class student:

    def __init__(self,rno,name):
        self.rno = rno 
        self.name = name

    def display(self):          # instance method
        print(f"Rno : {self.rno} and Name : {self.name}")

student_obj = student(1,"Vinu")
# student_obj.info(1,"Vinu")
student_obj.display()

#! NOTE : It is recommended to not write logic inside the constructor



