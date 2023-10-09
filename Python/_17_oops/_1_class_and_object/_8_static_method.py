# function
# instance method
# constructor
# class method

# static method
# static method have nothing to do with instance variable and class variable
# it is purely used for local variable or normal logic , especially for API

class demo:

    school = "TVM"

    def __init__(self,name):
        self.name = name

    @staticmethod
    def stats(sname):
        return f"Hey {sname}"
    
obj = demo("Edyoda")
print(obj.stats("Bharati"))