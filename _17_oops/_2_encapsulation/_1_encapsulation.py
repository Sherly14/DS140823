# Encapsulation

# - it is use to bind attributes (variable) and behaviour (method) together into single unit.
# - it is use to access private member through public environment

class Car:

    def __init__(self,engine,brand,mileage):
        self.engine = engine
        self.brand = brand
        self.mileage = mileage

    def display(self):
        return f"Engine : {self.engine} \nBrand : {self.brand} \nMileage : {self.mileage}"
    
    # setter and getter
    def get_mileage(self):
        return self.mileage
    
    def set_mileage(self,mileage):
        self.mileage = mileage


obj = Car("Petrol Engine","BMW","35km/l")
data = obj.display()
print(data)

print()

mil = obj.get_mileage()
print("Mileage : ",mil)

obj.set_mileage("50km/l")

mil = obj.get_mileage()
print("Mileage : ",mil)


