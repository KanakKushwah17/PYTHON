"""
4.Unique Digit Security Scanner

A smart locker accepts only numbers whose all digits are unique.

Write a program using for-else loop to:

- Check every digit
- If any repeated digit found reject
- Else accept

Input:
57294

Output:
Valid Unique Code
"""
n=int(input("Enter any number :"))
for i in range(1,n>0):
    rem=n%10
    n=n//10
    nextrem=n%10
    if rem==nextrem:
        print("Reject")
        break
    nextrem=rem
else:
    print("Valid unique code")
