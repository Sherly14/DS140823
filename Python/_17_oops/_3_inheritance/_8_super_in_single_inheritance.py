# super - represents object of immediate parent class

class Dad:                           # parent class
    def flat(self):
        print("Flat")

    def car(self):
        print("Car")

    def bike(self):
        print("Dad's Bike")

class Son(Dad):                      # child class
    def bike(self):
        super().bike()
        print("Son's Bike")

    def mobile(self):
        print("Mobile")

son = Son()
son.bike()
son.mobile()
son.flat()
son.car()