"""
9.
Step Difference Number Analyzer

A mathematics research center studies hidden patterns inside numbers.
For every entered number, the system compares adjacent digits step by step.

Write a program to:

Find the absolute difference between every pair of adjacent digits
Display all step differences
Find the sum of all step differences
Find the largest step difference
If the sum of step differences is divisible by the number of digits, print Balanced Number
Otherwise print Unbalanced Number

Use loops wherever required.

Input:
57294
Output:
Step Differences: 2 5 7 5
Sum = 19
Largest = 7
Unbalanced Number
"""
num=int(input("Enter the number :"))
digits=num
sum=0
big=0
count=0
while num>9:
    rem1=num%10
    num=num//10
    rem2=num%10
    diff=abs(rem1-rem2)
    rem=diff%10
    print("difference :",diff)
    sum=sum+diff
    count=count+1

    if diff> big:
        big=diff
print("Sum is :",sum)
print("Largest Digit =", big)
if sum%count==0 and count!=0:
    print("balanced number")
else:
    print("Unbalanced number")