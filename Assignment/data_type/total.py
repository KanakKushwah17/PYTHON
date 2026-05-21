"""
Assignment 10: Percentage Calculator

Write a Python program that:

Accepts total marks and obtained marks.
Calculates percentage.

Input:
Total = 500
Obtained = 400

Output:
Percentage = 80%
"""

total= int(input("Total marks :"))
Obt=int(input("obtained marks :"))
per=(Obt/total)*100
print("percentage : ",per)