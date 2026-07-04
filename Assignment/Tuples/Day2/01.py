"""
=====================================================================
QUESTION 1: EMPLOYEE SALARY ANALYSIS
====================================

A company wants to store employee details and generate salary reports using NamedTuple.

Fields:
emp_id, emp_name, department, salary

Requirements:

1. Read N employee details from the user and store them in a list of NamedTuples.

---

2. Display all employee details.

---

3. Find and display the employee with the highest salary.

---

4. Find and display the employee with the lowest salary.

---

5. Calculate and display the average salary of all employees.

---

6. Accept a department name from the user and display all employees belonging to that department.

---

Test Case:

Input:
Enter number of employees: 4

101 Rahul IT 50000
102 Priya HR 45000
103 Amit IT 70000
104 Neha Finance 60000

Enter department: IT

Expected Output:
Highest Salary Employee:
103 Amit IT 70000

Lowest Salary Employee:
102 Priya HR 45000

Average Salary:
56250.0

Employees in IT Department:
101 Rahul IT 50000
103 Amit IT 70000
"""

from collections import namedtuple
Employee=namedtuple("Employee",["emp_id", "emp_name", "department", "salary"])

n=int(input("Enter number of students: "))
employee=[]

for i in range(n):
    idd=int(input("Enter Employee ID: "))
    na=input("Enter employee Name: ")
    d=input("Enter department: ")
    sal=int(input("Enter Salary: "))

    employee.append(Employee(idd,na,d,sal))

print("===============Employee Details===============")
for e in employee:
    print(e.emp_id,e.emp_name,e.department,e.salary)

max=employee[0]
print("=======================Highest Salary Employee===========")
for e in employee:
    if e.salary>max.salary:
        max=e
print("Highest Salary Employee:",max.salary)


min=employee[0]
print("===============Lowest Salary Employee=================")
for e in employee:
    if e.salary<min.salary:
        min=e
print("lowest Salary Employee:",min.salary)

sum=0
print("=================Average Salary======================")
for e in employee:
    sum=sum+e.salary
total=sum/n
print("Total Salary Average :",total)



print("==========Department===========")
dep = input("\nEnter department name: ")
for e in employee:
    if e.department== dep:
        print(e.department)