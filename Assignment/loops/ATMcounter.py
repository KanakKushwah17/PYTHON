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
rs=int(input("enter the amount of rs"))
count=0
for i in range(1,rs+1):
    if i%100==0:
        count+=1
print("Notes = ",count)
