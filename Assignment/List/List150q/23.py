"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.
Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
"""

n=int(input("Enter the number for nums 2: "))
num=[]
for i in range(n):
    num.append(int(input("Enter the number: ")))
k=int(input("Enter the target value: "))
count=0
for i in range(len(num)):
    for j in range(i,len(num)):
        sub=num[i:j+1]
        sum = 0
        for l in sub:
            sum=sum+l
        if sum==k:
            count=count+1
print(count)