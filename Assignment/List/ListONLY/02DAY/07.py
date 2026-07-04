"""
7.
Factory Production – Factorial Expansion List

Problem Statement

A factory produces items where production capacity is defined using factorial growth.

Given a list of numbers, replace each number with its factorial value.

Then perform analysis on the resulting list.

Tasks:

Convert each element to factorial
Find sum of all factorial values
Find maximum factorial value
Count how many factorial values are even

Input:
A list of integers

Example 1

Input:
[3, 4, 5]

Processing:
3! = 6
4! = 24
5! = 120

Output:
[6, 24, 120]
Sum = 150
Max = 120
Even Count = 3
"""

n=int(input("Enter the size of the list: "))
arr=[]
for i in range(n):
    x=int(input("Enter the salary : "))
    arr.append(x)
print(arr)

factlist=[]
for num in arr:
     j = 1
     fact=1
     while j<=num:
        fact=fact*j
        j=j+1
     factlist.append(fact)
sum=0
for i in factlist:
    sum=sum+i
print(sum)

max=factlist[0]

for i in factlist:
    if max>i:
        max=i
print(max)


count = 0

for i in factlist:
    if i % 2 == 0:
        count = count + 1

print("Even Count =", count)