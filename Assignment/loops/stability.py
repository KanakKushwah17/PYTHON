"""5.Number Stability Analyzer

A science lab studies whether digits are in increasing order.

Write a program using for-else loop:

- If every next digit is greater than previous print Stable Number
- Else Unstable Number

Input:
12359

Output:
Stable Number
"""
n=int(input("Enter a number: "))
prev=10
while n>0:
      rem=n%10
      if rem>=prev:
          print("Unstable Number")
          break
      prev=rem
      n=n//10
else:
    print("Stable Number")









