"""
Assignment 4: Travel Distance Calculation

A person is traveling at a constant speed. Time is given in hours and minutes. Convert total time into hours and calculate distance.

Input:
Speed = 60 km/hr
Time = 2 hours 30 minutes

Expected Output:
Total Time = 2.5 hours
Distance = 150.0 km
"""
speed=int(input("Enter the speed : "))
hours,minutes=map(int,input("Enter the Time in hours and minutes : ").split())
print('{}hours{}minutes'.format(hours,minutes))
minutes=minutes/60
hours=hours+minutes
print("Total time :",hours)
Distance=hours*speed
print("Distance :",Distance)
