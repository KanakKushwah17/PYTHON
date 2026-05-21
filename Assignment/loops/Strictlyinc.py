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
n=int(input("Enter a number: "))
rev=0
prev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
pos=1
while rev>0:
    rem=rev%10
    if rem<=prev:
        print("Break at position",pos-1)
        print("Not Increasing Number")
        break
    prev=rem
    rev=rev//10
    pos=pos+1
else:
    print("Strictly Increasing Number")

