"""
6.

A security system logs employee entry IDs during a day.

Only prime-numbered IDs are considered valid VIP entries.

Tasks:

Extract all prime IDs from the list
Find the sum of prime IDs
Find the maximum prime ID
Count how many prime entries exist

Input:
A list of integers (may contain duplicates and non-prime numbers)

Example 1

Input:
[12, 5, 7, 9, 11, 14, 17]

Output:
Prime IDs = [5, 7, 11, 17]
Sum = 40
Max = 17
Count = 4

Example 2

Input:
[4, 6, 8, 10]

Output:
Prime IDs = []
Sum = 0
Max = -1
Count = 0

"""
n=int(input("Enter the size of the list: "))
arr=[]
for i in range(n):
    x=int(input("Enter the salary : "))
    arr.append(x)
print(arr)

prime_count=0

list_prime=[]
for num in arr:
    k = 1
    if num<=1:
        continue
    for i in range(2,num//2+1):
        if num%i==0:
            k=0
            break

    if k==1:
        list_prime.append(num)
        prime_count=prime_count+1
print("List of prime number :",list_prime)
print("Prime count",prime_count)
sum=0
for i in list_prime:
    sum=sum+i
print("prime sum:",sum)
largest_prime=0
for i in list_prime:
    if i>largest_prime:
        largest_prime=i
print("Largest Prime number :",largest_prime)
