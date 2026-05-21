"""
Assignment 5: Salary Breakdown

An employee wants to calculate salary per day and per hour.

Input:
Monthly salary = 36000
Working days = 24
Working hours per day = 8

Expected Output:
Salary per day = 1500.0
Salary per hour = 187.5

---
"""
salary=int(input("Monthly salary :"))
workingdays=int(input("Working days : "))
workinghour=int(input("Working hour per day : "))
salary=salary/workingdays
print("Salary : ",salary)
salary=salary/workinghour
print("Working hours : ",salary)


