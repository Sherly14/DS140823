class Dad:   
    def __init__(self,name):
        print("Dad",name)
    
    def flat(self):
        print("Flat")

class Son(Dad): 
    def __init__(self,name,rno):
        super().__init__(name)
        print("Son",rno)

    def bike(self):
        print("Bike")

son = Son("Raj",10)
son.bike()
son.flat()
