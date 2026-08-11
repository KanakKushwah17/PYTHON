"""Assignment 3.

Create a parent class Bank with a method getInterestRate() that returns 0.

Create subclasses:

SBI that overrides getInterestRate() to return 5.

ICICI that overrides getInterestRate() to return 6.

Axis that overrides getInterestRate() to return 7.

In the Main class, demonstrate method overriding by calling getInterestRate() on different bank objects.

    """
    
class Bank():
    def getInterestRate(self):
        return 0
class SBI(Bank):
    def getInterestRate(self):
        return 5
    
class ICICI(Bank):
    def getInterestRate(self):
        return 6
class Axis(Bank):
    def getInterestRate(self):
        return 7
print(f"Interest rate of Bank is {Bank().getInterestRate()}%")
print(f"Interest rate of SBI is {SBI().getInterestRate()}%")
print(f"Interest rate of ICICI is {ICICI().getInterestRate()}%")
print(f"Interest rate of Axis is {Axis().getInterestRate()}%")