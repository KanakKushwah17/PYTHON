"""You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
    """
    
"""rows=int(input("enter the number of rows:"))
cols=int(input("enter the number of columns:"))
matrix=[]
for i in range(rows):
    rows=[]
    for j in range(cols):
        rows.append(int(input("enter row number:")))
    matrix.append(rows)
print("Elements are :")
for i in matrix:
    for j in i:
        print(j,end=" ")
    print()"""
    
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
flag=0
for sublist in matrix:
    for element in sublist:
        if element==target:
            flag=1
if flag==1:
    print("true")
else:
    print("false")
       
          
