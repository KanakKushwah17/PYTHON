"""a=[1,2,[3,4],5,6]
print(a)
print(a[0])
print(a[2])
print(a[2][1])"""

"""a=[
    [10,20,30],
    [40,50,60],
    [70,80,90]
]
print(a[0])
print(a[1])
print(a[2])

for i in a:#i is row 
    print(i)
    """

"""
a=[
    [10,20,30],
    [40,50,60],
    [70,80,90]
]

for i in a:
    for j in i:
        print(j,end=" ")
    print()
"""

"""
a=[
    [10,20,30],
    [40,50,60],
    [70,80,90]
]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
    print()
"""

"""a=[
    [10,20,30],
    [40,50,60],
    [70,80,90]
]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[j][i],end=" ")
    print()"""

"""
a=[
    [10,"deepika"],
    [40],
    [70,80,90],
    ["abc","xyz"]
]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
    print()
"""

"""a=[
    [10,"deepika"],
   [40,50,60],
   [70],
   ["abc","xyz"]
   ]
print(a)

a[1][0]="virat"
print(a)
"""

"""
rows=int(input("enter the number of rows:"))
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


#WAP To sum of all matrix element
"""rows=int(input("enter the number of rows:"))
cols=int(input("enter the number of columns:"))
matrix=[]
for i in range(rows):
    rows=[]
    for j in range(cols):
        rows.append(int(input("enter row number:")))
    matrix.append(rows)
sum=0
print("Elements are :")
for i in matrix:
    for j in i:
        print(j,end=" ")
    print()
print(sum)
"""

"""rows=int(input("enter the number of rows:"))
cols=int(input("enter the number of columns:"))
matrix=[]
for i in range(rows):
    rows=[]
    for j in range(cols):
        rows.append(int(input("enter row number:")))
    matrix.append(rows)
sum=0
print("Elements are :")
i=0
while i < len(matrix):
    j=0
    while j <len(matrix[i]):
        sum=sum+matrix[i][j]
        j=j+1
    i=i+1
print(sum)
"""

"""
rows=int(input("enter the number of rows:"))
cols=int(input("enter the number of columns:"))
matrix=[]
for i in range(rows):
    rows=[]
    for j in range(cols):
        rows.append(int(input("enter row number:")))
    matrix.append(rows)
sum=0
for i in range(len(matrix)):
    sum=sum+matrix[i][i]
print("Sum : ",sum)
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
    print()
sum=0
for i in matrix:
    for j in i:
        if j%2!=0:
            sum=sum+j
print("Sum : ",sum)"""


"""
rows=int(input("enter the number of rows:"))
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
    print()
sum=0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j]%2!=0:
            sum=sum+matrix[i][j]
print("Sum : ",sum)"""

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
    print()

found=0
search=int(input("enter the search term:"))
for i in matrix:
    for j in i:
        if search==j:
            found=1
            break

if found==0:
    print("Number is not found")
else:
    print("Number is found")
    
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
    print()

for row in matrix:
    i=0
    j=len(row)-1
    while i<j:
        t=row[i]
        row[i]=row[j]
        row[j]=t
        i=i+1
        j=j-1

print("Elements are :")
for i in matrix:
    for j in i:
        print(j,end=" ")
    print()
"""




#ADD TWO MATRIX
"""rows=int(input("enter the number of rows:"))
cols=int(input("enter the number of columns:"))

matrix=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input("enter row number:")))
    matrix.append(row)

print("Elements are :")
for i in matrix:
    for j in i:
        print(j,end=" ")
    print()

print("MATRIX 2")
matrix2=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input("enter row number:")))
    matrix2.append(row)

print("Elements are :")
for i in matrix2:
    for j in i:
        print(j,end=" ")
    print()

#MATRIX3
print("MATRIX 3")
matrix3=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(())
    matrix3.append(row)

print("Elements are :")
for i in matrix3:
    for j in i:
        print(j,end=" ")
    print()

for i in range(len(matrix3)):
    for j in range(len(matrix3[i])):
        matrix3[i][j ]= matrix[i][j] + matrix2[i][j]

print("Elements are :")
for i in matrix3:
    for j in i:
        print(j,end=" ")
    print()
"""


"""
rows=int(input("enter the number of rows:"))
cols=int(input("enter the number of columns:"))

matrix=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input("enter row number:")))
    matrix.append(row)

print("Elements are :")
for i in matrix:
    for j in i:
        print(j,end=" ")
    print()

print("MATRIX 2")
matrix2=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input("enter row number:")))
    matrix2.append(row)

print("Elements are :")
for i in matrix2:
    for j in i:
        print(j,end=" ")
    print()

#MATRIX3
print("MATRIX 3")
matrix3=[]

for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(matrix[i][j] + matrix2[i][j])
    matrix3.append(row)

print("Elements are :")
for i in matrix3:
    for j in i:
        print(j,end=" ")
    print()
"""

r1=int(input("enter the number of rows:"))
c1=int(input("enter the number of columns:"))

matrix1=[]
for i in range(r1):
    row=[]
    for j in range(c1):
        row.append(int(input("enter row number:")))
    matrix1.append(row)

print("Elements are :")
for i in matrix1:
    for j in i:
        print(j,end=" ")
    print()



print("MATRIX 2")
r2=int(input("enter the number of rows:"))
c2=int(input("enter the number of columns:"))
matrix2=[]
for i in range(r2):
    row=[]
    for j in range(c2):
        row.append(int(input("enter row number:")))
    matrix2.append(row)

print("Elements are :")
for i in matrix2:
    for j in i:
        print(j,end=" ")
    print()

#MATRIX3
print("MATRIX 3")
if c1!=r2:
    print("Multiplication not possible")
else:
    result=[]
    for i in range(r1):
        row=[]
        for j in range(c2):
            row.append(0)
        result.append(row)
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j]=result[i][j]+matrix1[i][k]*matrix2[k][j]

    print("Result :")
    for row in result:
        print(row)