"""
Assignment 10: Time Conversion

Convert total seconds into hours, minutes, and seconds.

Input:
Total seconds = 7384

Expected Output:
Hours = 2
Minutes = 3
Seconds = 4
"""
import math
Seconds=int(input("enter seconds :"))

hours=Seconds/3600
print("Hours = ",math.floor(hours))

hours=Seconds%3600
min=hours/60
print("Min = ",math.floor(min))

min=hours%60
sec=min

print("Seconds = ",math.floor(sec))
