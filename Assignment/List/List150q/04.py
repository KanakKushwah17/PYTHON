"""
35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
"""

n=int(input("Enter the number: "))
k=int(input("Enter the target number: "))

num=[]
for i in range(n):
    num.append(int(input("Enter the number: ")))

flag=0
for i in range(len(num)):
    if num[i]==k:
        print(i)
        flag=1

if flag==0:
    print("The target number is not present in the list")



