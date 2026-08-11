"""Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3"""

"""n=int(input("Enter Numbers :   "))
nums=[]
for i in range(n):
    list=int(input("Enter list : "))
    nums.append(list)

print(nums)

        
        """
        

"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""

"""n=int(input("Enter the number: "))
k=int(input("Enter target k :"))
nums=[]
for i in range(n):
    nums.append(int(input("Enter the number: ")))
flag=0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            if abs(i-j)<=k:
                flag=1
if flag==1:
    print("true")
else:
    print("False")
    """

"""54. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:,


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],
                [5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
    """
"""
matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]
res=[]
for i in range(len(matrix[0])):
    res.append(matrix[0][i])

for i in range(1,len(matrix)):
    res.append(matrix[i][3])

for i in range(len(matrix)-1,-1,-1):
    res.append(matrix[2][i])
    
for i in range(len(matrix[0])-3,0,-1):
    res.append(matrix[i][0])
    
print(res)"""

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]

res = []

top = 0
bottom = len(matrix) - 1

left = 0
right = len(matrix[0]) - 1

while top <= bottom and left <= right:

    for i in range(left, right + 1):
        res.append(matrix[top][i])

    top += 1

    for i in range(top, bottom + 1):
        res.append(matrix[i][right])

    right -= 1

    if top <= bottom:

        for i in range(right, left - 1, -1):
            res.append(matrix[bottom][i])

        bottom -= 1

    if left <= right:

        for i in range(bottom, top - 1, -1):
            res.append(matrix[i][left])

        left += 1

print(res)