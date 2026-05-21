"""
1. Smart Shopping Mall Discount System
A shopping mall offers discounts based on customer type and purchase amount.
If the customer is premium, they get 20% discount when the amount is more than 5000, otherwise 10%.
If the customer is regular, they get 10% discount when the amount is more than 3000, otherwise 5%.
Write a program to calculate the final payable amount using inline if only.
"""
c_type=input("Enter any number :")
amount=int(input("Enter amount :"))
payable=amount-(amount*20)/100 if c_type=="premium" and amount>5000 else amount-(amount*10)/100 if c_type=="regular" else amount-(amount*5)/100
print("Payable : ",payable)