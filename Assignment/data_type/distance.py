"""
Assignment 15: Average Speed for Multiple Trips

Write a Python program that:

Accepts distance1, time1, distance2, time2.
Calculates average speed.

Input:
Distance1 = 60
Time1 = 1
Distance2 = 40
Time2 = 1

Output:
Average Speed = 50 km/h
"""
dist1=int(input("Enter the distance 1"))
time1=int(input("Enter the time1"))
dist2=int(input("Enter the distance 2"))
time2=int(input("Enter the time2"))
totaldis=dist1+dist2
totaltim=time1+time2
avg=totaldis/totaltim
print(avg)