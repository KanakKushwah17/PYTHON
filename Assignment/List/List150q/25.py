"""
Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
"""
n=int(input("Enter the number for nums: "))
num=[]
for i in range(n):
    num.append(int(input("Enter the number: ")))
target=int(input("Enter the target value: "))
flag=-1
new=[]
for i in range(len(num)):
    if num[i]==target:
        new.append(i)
        flag=0
if flag==-1:
    print([-1,-1])
else:
    print(new)