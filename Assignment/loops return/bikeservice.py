"""
9.
 Bike Service Kilometer Checker

A bike needs service every 3000 km.

Write a program to:

- Read travelled kilometers
- Print every service checkpoint till entered km

Input:
10000

Output:
3000 6000 9000
"""
n=int(input("Enter a number:"))
count=0
for i in range(1,n+1):
    if i%3000==0:
        print(i)
    n=n//10
