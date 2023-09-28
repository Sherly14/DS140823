# Multiple Inheritance - Multiple parent classes and single child class

class C:
    def procedure_feature(self):
        print("C is procedural language")

    def language(self):
        print("C")

class Cpp(object):
    def oops_feature(self):
        print("C++ is object oriented language")

    def language(self):
        print("Cpp")


class Python(Cpp,C):
    def both(self):
        print("Python has both the features")

    def language(self):
        print("Python")

python = Python()
python.procedure_feature()
python.oops_feature()
python.both()
python.language()

print(Python.mro()) # Method Resolution Order