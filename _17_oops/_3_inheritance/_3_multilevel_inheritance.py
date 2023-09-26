class Grandpa:
    def field(self):
        print("Field")

class Dad(Grandpa):
    def flat(self):
        print("Flat")

class Son(Dad):
    def bike(self):
        print("Bike")

son = Son()
son.bike()
son.flat()
son.field()