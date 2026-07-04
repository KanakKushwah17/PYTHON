"""
5. Equilibrium Index Finder
===========================

Scenario

Find an index where:

# Sum of elements on the left side

Sum of elements on the right side

Requirements

* Read N and list elements from user
* Find equilibrium index
* If not found, display message

Test Case 1

Input:
[1, 3, 5, 2, 2]

Output:
Equilibrium Index = 2

Explanation:
1 + 3 = 2 + 2

Test Case 2

Input:
[1, 2, 3]

Output:
No Equilibrium Index Found
"""

n=int(input("Enter the size of the list: "))
arr=[]
for i in range(n):
    x=int(input("Enter the marks: "))
    arr.append(x)
print(arr)

found=0

left=[]
right=[]
for i in range(len(arr)):
    left_sum = 0
    right_sum = 0
    for j in range(i):
         left_sum=left_sum+arr[j]
    for j in range(i+1,len(arr)):
         right_sum=right_sum+arr[j]
    if right_sum==left_sum:
        print("Equilibrium Index Found",i)
        found=1
if found==0:
    print("No Equilibrium Index Found")





