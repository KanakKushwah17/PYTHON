"""
3. Perfect Number Reward System

A gaming company rewards users if entered number is a Perfect Number.

(Perfect Number = sum of proper factors equals number)

Write a program using for-else loop to:

- Find sum of proper factors
- If sum equals number print Reward Unlocked
- Else print Try Again

Input:
6

Output:
Reward Unlocked
"""
n=int(input("Enter a number: "))
i=1
temp=n
sum_dig=0
for i in range (i,n):
    if n%i==0:
        print("factors ",i)
        sum_dig=sum_dig+i

if sum_dig==temp:
    print("Reward Unlocked")
else:
    print("Try Again")

