"""
Assignment 12: Change Return System

Write a Python program that:

Accepts amount.
Calculates ₹100, ₹50, ₹10 notes.

Input:
Amount = 380

Output:
₹100 x 3
₹50 x 1
₹10 x 3
"""
Amt=int(input("enter Amount :"))
hund=Amt//100
rem=Amt%100
fifty=rem//50
rem=Amt%50
ten=rem//10

print(f"rs 100 x {hund}")
print(f"rs 50 x {fifty}")
print(f"rs 10 x {ten}")
