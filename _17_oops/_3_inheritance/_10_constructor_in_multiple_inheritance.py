class C:
    def __init__(self,name):
        print("C",name)

class Cpp:
    def __init__(self,rno):
        print("Cpp",rno)

class Python(C,Cpp):
    def __init__(self,name,rno,address):
        C.__init__(self,name)
        Cpp.__init__(self,rno)
        print("Python",address)
        
python = Python("Amandip",10,"Vikhroli E")