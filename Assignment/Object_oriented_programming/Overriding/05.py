"""Assignment 5:

Create a parent class Employee with a method calculateSalary() that prints "Base salary calculation for Employee."

Create subclasses:

Manager that overrides calculateSalary() to add a bonus to the base salary.

Developer that overrides calculateSalary() to calculate salary based on hours worked.

Demonstrate the overridden method in the Main class by creating an array of Employee objects and calling calculateSalary() on each.


    """

class Employee:
   def calculateSalary(self):
       print("Base salary calculation for Employee")
    
class Manager(Employee):
    def calculateSalary(self):
        base_salary = 50000
        bonus = 10000
        print(f"Manager salary: {base_salary + bonus}")
        
class Developer(Employee):
    def calculateSalary(self):
        hours = 160
        rate = 300
        print(f"Developer salary: {hours * rate}")
    
m=Manager()
m.calculateSalary()

d=Developer()
d.calculateSalary()
    