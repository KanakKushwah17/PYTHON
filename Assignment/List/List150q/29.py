"""
11. Container With Most Water
You are given an integer array height of length n. There are n vertical lines drawn such
that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container,
such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
"""
n = int(input("Enter the number of elements: "))
nums = []

for i in range(n):
    nums.append(int(input("Enter the number: ")))

max_area = 0

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        width = j - i
        height = min(nums[i], nums[j])
        area = width * height

        if area > max_area:
            max_area = area

print("Maximum water stored:", max_area)
