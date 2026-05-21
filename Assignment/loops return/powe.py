"""
7. Power of a Number
A scientific calculator app is used by engineering students for repeated multiplication operations. It should calculate the value of a number raised to a given power.
Write a program to calculate n raised to power p using loops.

Input:
2 5

Output:
32
"""
n=int(input("Enter a number:"))
powe=1
power=int(input("Enter a power:"))
for i in range(n,power+2):
      powe=n*powe
print(powe)

