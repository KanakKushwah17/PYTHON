"""Assignment 1: Speed Calculator

Write a Python program that:

Accepts distance (in km) and time (in hours).
Calculates speed.

Input:
Distance = 120
Time = 2

Output:
Speed = 60 km/h
----------------------------------------
"""

dist=int(input("Enter distance in km : "))
time=int(input("Enter time in hr : "))
speed=dist/time
print(f"speed : {speed}km/hr")