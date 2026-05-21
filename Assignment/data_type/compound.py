"""
Assignment 13: Compound Interest Calculator

Write a Python program that:

Accepts principal, rate, and time.
Calculates compound interest.

Input:
Principal = 1000
Rate = 10
Time = 2

Output:
Amount = 1210.0
Compound Interest = 210.0
"""
import math
P=int(input("Enter principal amount "))
R=int(input("Enter Rate "))
T=int(input("Enter Time in years "))

A=P* math.pow(1+(R/100),T)
print(A)
CI=A-P
print(CI)