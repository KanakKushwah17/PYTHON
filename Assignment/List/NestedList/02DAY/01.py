"""
1.
=========================================================
        MATRIX OPERATIONS MANAGEMENT SYSTEM
=========================================================


A data analysis company stores numerical information in matrix form.
To help employees perform matrix-related operations efficiently,
the company wants a menu-driven application.

The application should allow the user to:

1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

The user must enter the number of rows, columns, and all matrix
elements. The program should perform the selected operation and
display the result.

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user chooses Exit.

   1. Add Two Matrices
   2. Subtract Two Matrices
   3. Compare Two Matrices
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all elements of Matrix A and Matrix B from the user whenever
   required.

4. Based on the user's choice:

   Choice 1 - Add Two Matrices
   --------------------------------
   Add corresponding elements of both matrices and display
   the resultant matrix.

5. Choice 2 - Subtract Two Matrices
   --------------------------------
   Subtract corresponding elements of Matrix B from Matrix A
   and display the resultant matrix.

6. Choice 3 - Compare Two Matrices
   --------------------------------
   Check whether both matrices are equal.

   Two matrices are considered equal if:
   - They have the same dimensions.
   - Corresponding elements are equal.

   Display:
   "Matrices are Equal"
   or
   "Matrices are Not Equal"

7. Choice 4 - Exit
   --------------------------------
   Display:
   "Thank You for Using Matrix Operations Management System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

Enter your choice: 1

Enter number of rows: 2
Enter number of columns: 2

Enter Matrix A:
1 2
3 4

Enter Matrix B:
5 6
7 8

Result Matrix:
6 8
10 12

---------------------------------------------------------

Menu
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

Enter your choice: 3

Enter number of rows: 2
Enter number of columns: 2

Enter Matrix A:
1 2
3 4

Enter Matrix B:
1 2
3 4

Output:
Matrices are Equal

---------------------------------------------------------

Menu
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

Enter your choice: 4

Output:
Thank You for Using Matrix Operations Management System

=========================================================

"""

rows=int(input("enter the number of rows:"))
cols=int(input("enter the number of columns:"))

matrix=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input("enter row number:")))
    matrix.append(row)

print("Elements 1 :")
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

print("Elements 2 :")
for i in matrix2:
    for j in i:
        print(j,end=" ")
    print()

#MATRIX3
matrix3=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(())
    matrix3.append(row)
while True:
    print("MENU")
    print("1. Add Two Matrices")
    print("2. Subtract Two Matrices")
    print("3. Compare Two Matrices")
    print("4. Exit")
    choice=int(input("Enter your choice:"))
    match choice:
        case 1:
            #ADD
            for i in range(len(matrix3)):
                for j in range(len(matrix3[i])):
                    matrix3[i][j]= matrix[i][j] + matrix2[i][j]
            print("ADDITION :")
            for i in matrix3:
                for j in i:
                    print(j,end=" ")
                print()
        case 2:
            #SUB
            for i in range(len(matrix3)):
                for j in range(len(matrix3[i])):
                    matrix3[i][j]= matrix[i][j] - matrix2[i][j]

            print("SUBTRACTION :")
            for i in matrix3:
                for j in i:
                    print(j,end=" ")
                print()
        case 3:
            #COMPARE TWO MATRIX
            found=0
            for i in range(len(matrix3)):
                for j in range(len(matrix3[i])):
                    if matrix[i][j]!=matrix2[i][j]:
                        found=1
            if found==1:
                print("Matrix not equal ")
            else:
                print("Matrix equal ")
        case 4:
            print("EXIT")
            break
