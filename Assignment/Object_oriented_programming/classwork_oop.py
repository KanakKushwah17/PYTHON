"""class Student:
    pass
s1=Student()
"""

"""class Car:
    pass
c1=Car()
c2=Car()"""


"""class Mobile:
    def __init__(self):
        print("Constructor called ")
    
m1=Mobile()"""

"""class Student:
    def __init__(self,name):
       self.name=name

s1=Student("kanak")"""

"""class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

e1=Employee("Kanak",90000000)
    """
"""    
class Book:
    def __init__(self ,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    
b1 = Book("Python", "Guido", 500)
    """

"""class Student:
    def __init__(self,name):
       self.name=name
    
    def show(self):
        print("Name : ",self.name)

s1=Student("kanak")
s1.show()"""

"""class Car:
    def __init__(self,company,model):
        self.company=company
        self.model=model
    def display(self):
        print("Company :",self.company)
        print("Model : ",self.model)
    
c1=Car("Tata","Nexon")
c1.display()"""
"""
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    
    def area(self):
        self.a=self.length*self.width
        print("Area :",self.a)
    
r1=Rectangle(10,5)
r1.area()"""


"""class Animal:
    def sound(self):
        print("Sound")
    
class Cat():
    def sound(self):
       print("Meow")

a1=Cat()
a1.sound()"""


"""class Parent:
    def __init__(self):
        print("Hello parents")
    
class Class(Parent):
    def __init__(self):
        print("Hello  ")
        
        
c = Class()
"""
"""
class Parent:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Parent Name:", self.name)

class Child(Parent):
    def __init__(self, name):
        super().__init__(name)

    def display(self):
        super().display()
        print("Child Name:", self.name)

c = Child("Kanak")
c.display()"""

""" Create Shape, Circle, and Rectangle classes. Override area(). """

"""class Shape:
    def area(self):
        pass
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius  = radius
         
    def area(self):
        a=3.14*self.radius*self.radius
        return a

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    
    def area(self):
        a=self.length*self.width
        return a
    
    
c = Circle(2)
print(c.area())

r=Rectangle(2,3)
print(r.area())
    """
    
"""class Vehicle:
    def start(self):
        print("Vehicle start")
    
class Car(Vehicle):
    def start(self):
        print("Car start")
    
class Bike(Vehicle):
    def start(self):
        print("Bike start")
    
c=Car()
c.start()

b=Bike()
b.start()
"""
"""
class A:
    def a(self):
        print("A")
    
class B(A):
    def a(Self):
        super().a()
        print("B")
    
class C(B):
    def a(self):
        super().a()
        print("C")
c=C()
c.a()"""


        