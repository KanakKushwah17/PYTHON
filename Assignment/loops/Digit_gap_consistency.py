"""
4.
1. Digit Gap Consistency Checker

A number analysis system checks whether the gap between digits follows a consistent pattern.

Write a program to:

Find the absolute difference between first two digits
Compare this difference with all next adjacent digit differences
If any difference is not equal to the first difference, stop using break
Display:
- Initial gap
- Whether all gaps are same or not

Input:
8642

Output:
Initial Gap = 2
Consistent Pattern

Input:
97531

Output:
Initial Gap = 2
Consistent Pattern

Input:
5321

Output:
Initial Gap = 2
Pattern Break Detected
"""
n=int(input("Enter a number:"))

rem=n%10
n=n//10

prev=n%10
gap=abs(rem-prev)
n=n//10

flag=1
while n>0:
    rem=n%10
    if abs(prev-rem)!=gap:
        flag=0
        break
    prev=rem
    n=n//10
if flag==1:
    print("Initial Gap",gap)
    print("consistent pattern")
else:
    print("Pattern Break Detected")
