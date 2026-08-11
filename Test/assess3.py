matrix = [
    [1,2,3],
    [4,5,6]
    ]

# for row in matrix:
#     for elements in row:
#         print(elements,end=" ")
#     print()

# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         print(matrix[i][j],end=" ")
#     print()
    
    

matrix1=[]
r,c = map(int,input("Enter Rows and Columns:").split())
for i in range(r):
    row=[]
    for j in range(c):
        row.append(int(input(f"{i+1} ka {j+1} :")))
    matrix1.append(row)
    
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        print(matrix1[i][j],end=" ")
    print()
    
    
    
    
matrix1 = []

r, c, d = map(int, input("Enter Rows, Columns and Depth: ").split())

for k in range(d):
    layer = []
    print(f"\nEnter values for Layer {k+1}:")

    for i in range(r):
        row = []
        for j in range(c):
            row.append(int(input(f"{k+1} ka {i+1} ka {j+1} : ")))
        layer.append(row)

    matrix1.append(layer)


# Print 3D matrix
for i in range(d):
        for j in range(r):
            for k in range(c):
                print(matrix1[i][j][k], end=" ")
        print()