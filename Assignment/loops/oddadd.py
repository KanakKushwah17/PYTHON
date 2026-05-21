"""
1. Product of Odd Numbers up to N

A puzzle game rewards players by multiplying odd numbers up to n.
Write a program using loops to find product of odd numbers.

Input:
5

Output:
15
"""
digit=int(input("Enter the digit :"))
mult=1

for i in range(1,digit+1):
    if i%2!=0:
        mult=mult*i
print("Output :",mult)