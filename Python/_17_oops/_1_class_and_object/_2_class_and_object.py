# self - represents the object of current class

class shape:
    def triangle(self):
        height = int(input("Enter height: "))
        base = int(input("Enter base: "))
        area = base*height/2
        return(area)
    
    def square(self):
        side = int(input("Enter side: "))
        area = side ** 2
        return(area)
    
    def circle(self):
        radius = int(input("Enter radius: "))
        area = 3.14 * (radius ** 2)
        return(area)
    
obj = shape()
print("Area of triangle is: ",obj.triangle())
print("Area of square is: ",obj.square())
print("Area of circle is: ",obj.circle())

