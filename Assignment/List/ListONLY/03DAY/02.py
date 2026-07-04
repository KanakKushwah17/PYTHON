"""
2. First Repeating Number
=========================

Scenario

A security system logs employee IDs.

Find the first ID that repeats in the list.

Requirements

* Read N and list elements from user
* Find the first repeating number
* If no repeating number exists, display an appropriate message

Test Case 1

Input:
[10, 5, 3, 4, 3, 5]

Output:
First Repeating Number = 3

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Repeating Number Found
"""

n=int(input("Enter the size of the list: "))
arr=[]
for i in range(n):
    x=int(input("Enter the marks: "))
    arr.append(x)
print(arr)
list=0
for i in range(len(arr)):
    count=0
    for j in range(0,i+1):
        if arr[i]==arr[j]:
            count+=1
    if count > 1:
        list = arr[i]
        break
if list != 0:
    print(" FIRST Repeating Number", list)
else:
    print("Non-Repeating Number")