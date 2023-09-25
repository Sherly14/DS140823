# Constructor

# is a special kind of method
# it is represented by __init__()
# it is use to create object of class
# it is use to initialize instance variable - hold
# it gets called automatically when the object is created

class demo:
    def __init__(self,name):             # special kind of method
        print("Constructor1",name)

demo_obj = demo("Bharati")


# PVM - Python Virtual Machine

# Types of contructors
# 1. Default Constructor - if you don't have __init__ method in your class, 
#                          PVM provides default constructor to create the object
# 2. Zero Constructor - without any parameter
# 3. Parameterized Constructor - with parameter
