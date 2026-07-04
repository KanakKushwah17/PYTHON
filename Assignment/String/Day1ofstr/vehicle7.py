"""
7.
Vehicle Number Plate Checker

The traffic department wants to validate vehicle registration numbers.

Conditions:
- First 2 characters should be alphabets
- Next 2 should be digits
- Total length should be 10

Input:
Enter vehicle number: MP04AB1234

Output:
Valid Vehicle Number
"""
num=input("Enter vehicle number: ").upper()
valid=False
if num[0]>='A' and num[0]<='Z' and num[1]>='A' and num[1]<='Z' and num[2]>='0' and num[2]<='9' and num[3]>='0' and num[3]<='9' :
    valid=True

    if len(num)==10:
        valid=True
    else:
        valid=False
if valid==True:
    print("Valid Vehicle Number")
else:
    print("Not Valid Vehicle Number")