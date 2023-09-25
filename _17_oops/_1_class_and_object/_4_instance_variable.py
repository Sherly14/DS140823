# instance variable
# define inside the method/constructor with 'self' as prefix
# scope - throughout the class


class student:
    def info(self):                     # instance methods
        self.rno = 90
        self.name = "Bharati"
        
    def display(self):
        print(f"Rno : {self.rno} and Name : {self.name}")

student_obj = student()
student_obj.info()
student_obj.display()

print(student_obj.rno)
