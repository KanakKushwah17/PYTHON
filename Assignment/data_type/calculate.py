"""Assignment 3: Electricity Bill Calculator

Write a Python program that:

Accepts number of units.
Calculates bill (₹6 per unit).

Input:
Units = 100

Output:
Bill = 600
------------------------------------------
"""
calculate=int(input("Number of units : "))
bill=calculate*6
print(f"Electricity bill : {bill} ")