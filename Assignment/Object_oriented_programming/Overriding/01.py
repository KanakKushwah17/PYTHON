"""
Assignment 1: Shape Area Calculation

Create a parent class Shape with a method calculateArea() that prints "Area calculation not defined for Shape."

Create subclasses:

Circle that overrides calculateArea() to calculate and print the area of a circle.

Rectangle that overrides calculateArea() to calculate and print the area of a rectangle.

Write a Main class to demonstrate polymorphism using an array of Shape objects.
"""
class Shape:
    def calculateArea(self):
        print("Area calculation not defined for Shape")
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        
    def calculateArea(self):
        return 3.14*self.radius*self.radius

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    
    def calculateArea(self):
        return self.length*self.width

c=Circle(2)
print(c.calculateArea())

r=Rectangle(2,5)
print(r.calculateArea())

