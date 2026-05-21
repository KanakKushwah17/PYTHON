"""
2. Smallest Digit in Number
A manufacturing company prints serial numbers on products. During quality testing, the scanner needs to detect the smallest digit in the serial number to verify coding standards.
Write a program to find the smallest digit in a number using loops.

Input:
57294

Output:
Smallest Digit = 2
"""
pas = int(input("Enter the password :"))
min=9

while pas>0:
    rem=pas%10
    if rem<min:
        min=rem
    pas=pas//10
print("Smallest Digit =", min)
    