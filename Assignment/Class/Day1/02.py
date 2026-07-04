'''
Question 2: Electricity Bill Calculator
Scenario


An electricity company wants to generate monthly bills for its customers.

Requirements

Create a class named Customer with:

customer_id
customer_name
units_consumed

Initialize the values using a constructor.

Calculations
Cost per Unit = ₹8
Fixed Charge = ₹150
Total Bill = (Units × 8) + 150
Sample Input
Enter Customer ID : C101
Enter Customer Name : Amit Verma
Enter Units Consumed : 350
Sample Output
------ Electricity Bill ------
Customer ID       : C101
Customer Name     : Amit Verma
Units Consumed    : 350
Total Bill Amount : ₹2950.0

'''

class Electricity():
    def __init__(self,units):
        self.units=units
    def total_bill(self):
        self.bill=(self.units*8)+150

id=int(input("Enter customer id "))
customer_name=input("Enter customer name ")
units=int(input("enter Electricity bill "))
E1=Electricity(units)
E1.total_bill()
print("------ Electricity Bill ------")
print("Customer ID       : ",id)
print("Customer Name     : ",customer_name)
print("Units Consumed    : ",units)
print("Total Bill Amount : ₹",E1.bill)