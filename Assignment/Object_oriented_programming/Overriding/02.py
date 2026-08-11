"""2.

Create a parent class Animal with a method makeSound() that prints "Some generic sound."

Create subclasses:

Dog that overrides makeSound() to print "Woof Woof."

Cat that overrides makeSound() to print "Meow Meow."

In the Main class, use polymorphism to call makeSound() on different Animal objects.c
"""

class Animal():
    def makeSound(self):
       print("Some energic sound")

class Dog(Animal):
    def makeSound(self):
        print("woof woof")
    

class Cat(Animal):
    def makeSound(self):
        print("Meow Meow ")
    

class Main():
    def run(self):
        animals=[
            Animal(),
            Dog(),
            Cat()
        ]
    
        for animal in animals:
            animal.makeSound()
        
M=Main()
M.run()
        
