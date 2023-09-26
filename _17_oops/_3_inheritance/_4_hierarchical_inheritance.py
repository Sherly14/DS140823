# Hierarchical Inheritance - Single parent class and multiple child classes

class Dad:
    def dad_field(self):
        print("Dads field")


class Daughter(Dad):
    def daughter_field(self):
        print("Daughter_field")

class Son1(Dad):
    def son1_field(self):
        print("son1_field")

class Son2(Dad):
    def son2_field(self):
        print("son2_field")

son1=Son1()
son1.dad_field()
son1.son1_field()

son2=Son2()
son2.dad_field()
son2.son2_field()

daughter=Daughter()
daughter.dad_field()
daughter.daughter_field()