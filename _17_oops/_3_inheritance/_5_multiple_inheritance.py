# Multiple Inheritance - Multiple parent classes and single child class

class C:
    def procedure_feature(self):
        print("C is procedural language")

class Cpp:
    def oops_feature(self):
        print("C++ is object oriented language")

class Python(C,Cpp):
    def both(self):
        print("Python has both the features")


python = Python()
python.procedure_feature()
python.oops_feature()
python.both()