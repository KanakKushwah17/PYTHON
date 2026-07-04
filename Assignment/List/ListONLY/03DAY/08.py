"""
8. Majority Element Detector
============================

Scenario

Find an element occurring more than N/2 times.

Requirements

* Read N and list elements from user
* Find majority element
* If not present, display appropriate message

Test Case 1

Input:
[2, 2, 1, 2, 3, 2, 2]

Output:
Majority Element = 2

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Majority Element Found
"""


n=int(input("Enter the size of the list: "))
arr=[]
for i in range(n):
    x=int(input("Enter the marks: "))
    arr.append(x)
print(arr)

found=0
max=0
res=0
for i in range(n):
    count = 0
    for j in range(n):
        if arr[i]==arr[j]:
            count=count+1

        if count>n//2:
           res=arr[i]
           found=1
           break
if found==1:
    print("Majority Element Found",res)
else:
    print("No Majority Element Found")

