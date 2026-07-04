"""
4.
Palindrome Number List Checker
Scenario

A system checks lucky numbers which are palindromes.

Requirements
Check palindrome numbers
Store palindrome numbers in list
Count palindrome numbers
Find largest palindrome
Sort palindrome list
Test Cases

Input:
[121, 131, 20, 44, 55, 100]

Output:

Palindromes: [121, 131, 44, 55]
Count: 4
Largest: 131
Sorted: [44, 55, 121, 131]

"""
n=int(input("Enter a number: "))
arr=[]
for i in range(n):
    x=int(input("Enter a number: "))
    arr.append(x)
print(arr)

palindrome_list=[]
count_palindrome=0
for num in arr:
    temp = str(num)
    if temp[: :-1]==temp:
        palindrome_list.append(num)
        count_palindrome+=1

print("Palindrome :",palindrome_list)
print("Count",count_palindrome)

largest_palindrome=0
for i in palindrome_list:
    if largest_palindrome<i:
        largest_palindrome=i
print("Largest :", largest_palindrome)

print("Sorted",sorted(palindrome_list))

