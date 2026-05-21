"""
2.
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
n=int(input("Enter a number:"))
sum_digit=0
largest=0
temp=n
while n>9:
    rem=n%10
    n=n//10
    rem1=n%10
    diff=abs(rem-rem1)
    print("step difference : ",diff)
    sum_digit=diff+sum_digit
    if diff>largest:
        largest=diff
print("Largest =",largest)
print("sum =",sum_digit)
if temp%sum_digit==0:
    print("Balanced Number")
else:
    print("Unbalanced Number")