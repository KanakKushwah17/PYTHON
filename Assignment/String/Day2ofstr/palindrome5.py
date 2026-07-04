"""
Palindrome Product Code Checker

A factory wants to identify whether a product code reads the same forward and backward.

Input:
Enter product code: MADAM

Output:
Palindrome Code

Input:
Enter product code: PRODUCT

Output:
Not a Palindrome Code
"""
s1 = input("Enter product code: ").upper()
"""rev = s1[::-1]
if rev == s1:
    print("Palindrome Code")
else:
    print("Not a Palindrome Code")"""

rev=""

for i in s1:
    rev=i+rev

if rev==s1:
    print("Palindrome ")
else:
    print("Not palindrome ")
