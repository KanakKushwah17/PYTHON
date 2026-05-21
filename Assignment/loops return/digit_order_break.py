"""
2.
Digit Order Break Analyzer

A number validation system checks whether digits of an ID follow a strict increasing pattern. The moment the pattern breaks, the system stops further checking.

Write a program to:

Traverse the digits from left to right
Check whether each digit is greater than the previous digit
If the pattern breaks at any point, stop checking further using break
Display the position where the order breaks (1-based index)
If no break occurs, print Strictly Increasing Number

Use loops and break wherever required.

Input:
12357

Output:
Strictly Increasing Number

Input:
12342

Output:
Break at position = 4
Not Increasing Number
"""
n=int(input("Enter a number "))
prev=n%10
n=n//10
flag=True
while n>0:
    curr=n%10
    n=n//10
    if curr>prev:
        flag=False
        print("Break at position ",s)
        print("Not Increasing Number")
        break
    else:
        flag=True
if flag==True:
    print("Strictly Increasing Number")

