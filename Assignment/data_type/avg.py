"""
Assignment 5: Average Marks Calculator

Write a Python program that:

Accepts marks of 3 subjects.
Calculates average.

Input:
Marks = 80, 90, 70

Output:
Average = 80.0
"""

sub1,sub2,sub3 = map(int,input("Enter three subject numbers : ").split())
avg=(sub1+sub2+sub3)/3)
print("Average : ",avg)

