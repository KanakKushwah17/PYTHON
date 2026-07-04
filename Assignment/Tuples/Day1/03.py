"""

3.

MATRIX PERFORMANCE EVALUATION SYSTEM

A company records the monthly performance scores of employees in a matrix format. Each row represents an employee and each column represents a month.

The HR department wants a menu-driven application to analyze employee performance.

Menu
1. Find Employee with Highest Total Score
2. Find Month with Lowest Average Score
3. Display Employee-wise Maximum Score
4. Exit
Requirements
Choice 1 – Find Employee with Highest Total Score
Calculate the sum of each row.
Display the employee number having the highest total score.
Choice 2 – Find Month with Lowest Average Score
Calculate the average of each column.
Display the month having the lowest average score.
Choice 3 – Display Employee-wise Maximum Score
Find and display the maximum value present in each row.
Sample Input
10 20 30
40 50 60
25 35 45
Output
Employee 2 has Highest Total Score = 150

Month 1 Average = 25
Month 2 Average = 35
Month 3 Average = 45

Employee 1 Max Score = 30
Employee 2 Max Score = 60
Employee 3 Max Score = 45

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

while True:
    print("============================\n")
    print("1. Highest Total score")
    print("2. Month with lowest average score ")
    print("3. maximum value present in each row")
    print("4. Exit")
    choice=int(input("Enter your choice:"))
    match choice:
        case 1:
            max=0
            for i in range(rows):
                sum=0
                for j in range(cols):
                    sum=sum+matrix[i][j]
                if sum>max:
                    max=sum
            print("Employee",i+1,"has Highest Total Score =",max)

        case 2:
            for i in range(cols):
                 sum = 0

                 for j in range(rows):
                     sum = sum + matrix[j][i]
                 avg=sum/cols
                 print("Month ",i+1,"Average Score =",avg)
        case 3:
            for i in range(rows):
                max=0
                for j in range(cols):
                    if matrix[i][j]>max:
                        max=matrix[i][j]
                print("Month",i+1,"Hieghest row Score =",max)
        case 4:
            print("Exit")
            break