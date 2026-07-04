"""
2.Employee Salary Processing
Store employee salaries in a List and calculate details.

Requirements:

Store salaries
Find average salary
Display salaries greater than average
Remove salaries below 15000

Test Cases:

Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
Input: [15000, 15000, 15000] → Average = 15000
Input: [5000, 7000] → Remaining List = []

"""
n=int(input("Enter the size of the list: "))
arr=[]
for i in range(n):
    x=int(input("Enter the salary : "))
    arr.append(x)

avg=0
sum=0

for i in arr:
    sum=sum+i
    avg=sum/n

print("The average salary is",avg)

for i in arr:
    if i>avg:
        print("Above average ",i)

