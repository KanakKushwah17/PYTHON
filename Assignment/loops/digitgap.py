"""
4.Digit Gap Analyzer

A system analyzes the gap between consecutive digits.

Write a program to:

Traverse digits from left to right
Find the absolute difference between current digit and next digit
Display each difference
Count how many differences are greater than 2
Find the maximum difference
If all differences ≤ 2 → print Smooth Number
Else → print Irregular Pattern

Input:
86421

Output:
Differences: 2 2 2 1
Count (>2) = 0
Max Difference = 2
Smooth Number

"""
n=int(input("Enter a number: "))
rev=0
prev=0
count=0
maxgap=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
while rev>0:
    rem=rev%10
    rev=rev//10
    prev=rev%10
    gap=abs(rem-prev)
    print("Difference",gap)
    if gap>2:
        count=count+1

    if gap > maxgap:
        maxgap = gap

    prev=rev
    rev=rev//10


print("Count (>2)",count)
print("Max Difference =", maxgap)
if count == 0:
    print("Smooth Number")
else:
    print("Irregular Pattern")




