"""
=====================================================================
QUESTION 2: STUDENT RESULT PROCESSING
=====================================

A training institute wants to manage student records using NamedTuple.

Fields:
roll_no, name, course, marks

Requirements:

1. Read N student records from the user and store them in a list of NamedTuples.

---

2. Display all student details.

---

3. Find and display the topper of the class.

---

4. Count and display the number of students scoring above 80 marks.

---

5. Calculate and display the average marks.

---

6. Accept a course name from the user and display all students enrolled in that course.

---

Test Case:

Input:
Enter number of students: 4

1 Ravi Python 85
2 Anjali Java 78
3 Karan Python 92
4 Pooja Testing 88

Enter course: Python

Expected Output:
Topper:
3 Karan Python 92

Students Above 80:
3

Average Marks:
85.75

Students in Python Course:
1 Ravi Python 85
3 Karan Python 92
"""
from collections import namedtuple
Students=namedtuple("Students",["roll_no","s_name", "course", "marks"])

n=int(input("Enter number of students: "))
Student=[]

for i in range(n):
    r=int(input("Enter roll number: "))
    na=input("Enter student Name: ")
    co=input("Enter Course: ")
    m=int(input("Enter marks: "))

    Student.append(Students(r, na, co, m))

print("=====Student details ======")
for s in Student:
    print(s.roll_no, s.s_name, s.course, s.marks)

print("=====Topper======")
max = Student[0]

for s in Student:
    if s.marks > max.marks:
        max = s

print(max.roll_no, max.s_name, max.course, max.marks)

print("======Toppers in the class =======")

count=0
for s in Student:
    if s.marks<80:
        count=count+1
print("count",count)

print("======Average marks==============")
sum=0
for s in Student:
    sum=sum+s.marks
avg=sum/n
print("average marks",avg)

print("======Students in which field ======")
cour=input("Enter course name: ")
for s in Student:
    if s.course == cour:
        print(s.roll_no, s.s_name, s.course, s.marks)