"""
7.
 Alternate Digit Prime Checker

A math lab adds alternate digits from right side.

Write a program to:

- Find sum of alternate digits
- Check whether sum is Prime or Not

Input:
12345

Output:
Alternate Sum = 9
Not Prime
"""
n=int(input("Enter any number :"))
sum=0
while n>0:
    rem=n%10
    n=n//10
    sum=sum+rem
    n=n//10
print("Sum of alternate numbers :",sum)

x=0
if sum<=1:
    print("Not Prime")
else:
   i=2
   while i<sum//2+1:
        if sum%i==0:
            x=1
            break
        i=i+1
if x==0:
    print("Prime")
else:
    print("Not Prime")
