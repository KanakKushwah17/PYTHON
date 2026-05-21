"""
Assignment 11: Time Duration Adder

Write a Python program that:

Accepts hours, minutes, seconds.
Converts into total seconds.

Input:
Hours = 1
Minutes = 2
Seconds = 30

Output:
Total Seconds = 3750
"""
hours=int(input("enter hours :"))
min=int(input("enter min :"))
sec=int(input("enter seconds :"))
hours=hours*3600
min=min*60
totalsec=hours+sec+min
print("total second :",totalsec)