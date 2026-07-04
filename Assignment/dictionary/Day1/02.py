"""
2.
=========================================
EMPLOYEE DEPARTMENT COUNT
=========================

A company stores employee department names in a list.

employees = ["HR","IT","HR","Sales","IT","IT","Finance"]

Write a program to:

* Count how many employees belong to each department.
* Store the result in a dictionary.

Sample Output:
{'HR': 2, 'IT': 3, 'Sales': 1, 'Finance': 1}
"""

n=int(input("Enter the number of employees: "))

employee=[]
i=0
while i<n:
    name=input("Enter employee name: ")
    employee.append(name)
    i=i+1
d={}

for x in employee:
    if x in d:
        d[x]+=1
    else:
        d[x]=1
print(d)







