"""
8.
 ATM Note Counter

A bank ATM dispenses ₹100 notes.

Write a program to:

- Read withdrawal amount
- Count how many ₹100 notes needed using loop

Input:
700

Output:
Notes = 7
"""
n=int(input("Enter a number:"))
count=0
for i in range(1,n+1):
    if i%100==0:
        count=count+1
    n=n//10
print("Notes = ",count)
