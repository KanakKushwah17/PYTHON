"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true
"""
n=int(input("Enter the number: "))

num=[]
for i in range(n):
    num.append(int(input("Enter the number: ")))
new=[]
flag=0
for i in num:
    count=0
    for j in num:
        if i==j:
            count=count+1
    if count>=2:
        flag=1
        break
if flag==1:
    print("true")
else:
    print("false")
        
            
            
            
        
        