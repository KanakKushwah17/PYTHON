"""
5.
 Hospital Record System (Search Digit)

A hospital stores patient IDs as numbers. The administrator wants to verify whether a specific digit exists in a patient ID.
Task

Write a recursive function to determine whether a given digit is present.

Input
Enter Patient ID:
5837264

Enter Digit:
7
Output
Digit Found
"""
def even(a):
    if a==7:
        return True
    else:
        return a//10


def main():
    n=int(input("Enter Password:"))
    print(even(n))