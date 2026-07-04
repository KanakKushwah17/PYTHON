"""
1.
 Second Largest Unique Number
Scenario

A sports academy stores athlete scores in a list.

Find the second largest unique score.

Requirements
Read N and list elements from user
Find second largest unique number
If not available, display a message
Test Case

Input:

[10, 20, 30, 40, 40]

Output:

Second Largest = 30

"""
n=int(input("Enter the size of the list: "))
arr=[]
for i in range(n):
    x=int(input("Enter the marks: "))
    arr.append(x)
print(arr)

largest=0
for i in arr:
    if i>largest:
        largest=i

max=0
for i in arr:
    if i==largest:
        continue
    else:
        if i>max:
            max=i

print("Second largest",max)

