"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
"""
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

nums=[]
for i in range(num1):
    nums.append(int(input("Enter the number: ")))

nums2=[]
for i in range(num2):
    nums2.append(int(input("Enter the number: ")))

nums.sort()
nums2.sort()


new = []

for i in nums:
    for j in range(len(nums2)):
        if i == nums2[j]:
            new.append(i)
            nums2.pop(j)
            break

print(new)
