# Abstraction 
# means showing the functionality and hiding the implementation

# abstract method - method without body
# abstract class  - class with atleast one abstract method

# NOTE : creating object of abstract class is not allowed

from abc import abstractmethod,ABC

class laptop(ABC):
    def keyboard(self):
        print("Keyword")

    @abstractmethod
    def processor(self): # abstract method
        pass

class programmer(laptop):
    def processor(self):   # by overriding
        print("Processor")
        
obj = programmer()
obj.keyboard()
obj.processor()