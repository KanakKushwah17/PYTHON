"""
6.

Product Code Verification System

An e-commerce company wants to verify whether two product codes are rearranged versions of each other.

Conditions:
- Ignore spaces
- Ignore case sensitivity

Input:
Enter first product code: Dormitory
Enter second product code: Dirty Room

Output:
Both Product Codes are Matching

"""
s1=input("Enter first product code: ")
s2=input("Enter second product code: ")

rev=""
rev2=""

for i in s1:

    if i!=' ':

        if i>='A' and i<='Z':
            rev=rev+chr(ord(i)+32)

        else:
            rev=rev+i

for i in s2:

    if i!=' ':

        if i>='A' and i<='Z':
            rev2=rev2+chr(ord(i)+32)

        else:
            rev2=rev2+i

if sorted(rev)==sorted(rev2):
    print("Both Product Codes are Matching")

else:
    print("Product Codes are Not Matching")