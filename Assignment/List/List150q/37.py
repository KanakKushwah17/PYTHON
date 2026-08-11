"""
73. Set Matrix Zeroes
 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""
matrix = [[1,1,1],[1,0,1],[1,1,1]]

row_zero=[]
col_zero=[]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
            row_zero.append(i)
            col_zero.append(j)

for row in row_zero:
    for j in range(len(matrix[0])):
        matrix[row][j]=0

for col in col_zero:
    for j in range(len(matrix)):
        matrix[j][col]=0    

print(matrix)
