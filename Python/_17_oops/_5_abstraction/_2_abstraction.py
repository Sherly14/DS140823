from abc import ABC,abstractmethod

class college(ABC):

    def timing(self):
        print("10am - 1pm")

    @abstractmethod
    def exam_ticket(self):
        pass

class classroom_A(college):
    def exam_ticket(self):
        print("BSC Exam Ticket")

class classroom_B(college):
    def exam_ticket(self):
        print("BSC-IT Exam Ticket")

class classroom_C(college):
    def exam_ticket(self):
        print("BSC-CS Exam Ticket")

a = classroom_A()
a.timing()
a.exam_ticket()

b = classroom_B()
b.timing()
b.exam_ticket()

c = classroom_C()
c.timing()
c.exam_ticket()

c = classroom_C()