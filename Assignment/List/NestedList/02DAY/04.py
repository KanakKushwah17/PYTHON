"""
4.

=========================================================
        MATRIX DIAGONAL ANALYSIS SYSTEM
=========================================================

Scenario

A security company stores surveillance data in matrix form.
The analyst wants a menu-driven application to examine the
diagonal elements of the matrix and generate reports.

The application should allow the user to:

1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Display Main Diagonal Elements
   2. Display Secondary Diagonal Elements
   3. Compare Main and Secondary Diagonal Sums
   4. Exit

2. Read the size of a square matrix from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Display Main Diagonal Elements
   -----------------------------------------
   Display all elements present in the main diagonal.

5. Choice 2 - Display Secondary Diagonal Elements
   ----------------------------------------------
   Display all elements present in the secondary diagonal.

6. Choice 3 - Compare Main and Secondary Diagonal Sums
   ---------------------------------------------------
   Calculate the sum of both diagonals and display:

   - Main Diagonal Sum
   - Secondary Diagonal Sum
   - Which diagonal has the greater sum
   - Or whether both sums are equal

7. Choice 4 - Exit
   -----------------------------------------
   Display:
   "Thank You for Using Matrix Diagonal Analysis System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Enter size of matrix: 3

Enter matrix elements:

1 2 3
4 5 6
7 8 9

Menu
1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

Enter your choice: 1

Output:
Main Diagonal Elements:
1 5 9

---------------------------------------------------------

Enter your choice: 2

Output:
Secondary Diagonal Elements:
3 5 7

---------------------------------------------------------

Enter your choice: 3

Output:
Main Diagonal Sum = 15
Secondary Diagonal Sum = 15
Both Diagonal Sums are Equal

=========================================================

"""
rows=int(input("Enter size of matrix: "))
cols=int(input("Enter size of matrix: "))
matrix=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input("Enter number of rows and columns: ")))
    matrix.append(row)

for i in matrix:
    for j in i:
        print(j,end=" ")
    print()
while True:
    print("\n")
    print("1. Main Diagonal Elements")
    print("2. Secondary Diagonal Elements")
    print("3. Compare Main and Secondary Diagonal Sums")
    print("4. Exit\n")

    choice=int(input("Enter your choice: "))
    match choice:
        case 1:
            for i in range(rows):
                for j in range(cols):
                    if i==j:
                        print(matrix[i][j],end=" ")

        case 2:
            for i in range(rows):

                for j in range(cols):
                    if i+j==cols-1:
                        print(matrix[i][j], end=" ")

        case 3:
            sum1 = 0
            sum2 = 0
            for i in range(rows):
                for j in range(cols):

                    if i==j:
                       sum1=matrix[i][j]+sum1
                    if i+j==cols-1:
                       sum2=sum2+matrix[i][j]

            print("Main diagonal sum ",sum1,end=" ")
            print()
            print("Second diagonal sum ",sum2,end=" ")
            print()
            if sum1>sum2:
                print("Main diagonal is bigger")
            elif sum1<sum2:
                print("Secondary diagonal is bigger")
            elif sum1==sum2:
                print("Both diagonal equal")
            else:
                print("Not equal")
        case 4:
            print("Thank You for Using Matrix Diagonal Analysis System")
            break


