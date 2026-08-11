"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
    """


n = int(input("Enter the number of elements: "))

nums = []
for i in range(n):
    nums.append(int(input("Enter the number: ")))
res=[[]]
for i in range(len(nums)):
    for j in range(i,len(nums)):
            sub=nums[i:j+1]
            res.append(sub)
print(res)
