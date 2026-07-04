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

new1=""
new2=""
for ch in s1:
    if ch!= ' ':
        new1=new1+ch
for ch in s2:
    if ch!='':
        new2=new2+ch
if sorted(new1)==sorted(new2):
    print("Both products Codes are Matching ")
else:
    print("Both products codes are not matching ")
