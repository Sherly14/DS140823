# single inheritance - where single child class inheritances single parent class

class Dad:                           # parent class
    def flat(self):
        print("Flat")

    def car(self):
        print("Car")

class Son(Dad):                      # child class
    def bike(self):
        print("Bike")

    def mobile(self):
        print("Mobile")

son = Son()
son.bike()
son.mobile()
son.flat()
son.car()