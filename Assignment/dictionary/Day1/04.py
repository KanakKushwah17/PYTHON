"""
4.
=========================================
STUDENT GRADE ANALYSIS
======================

Store student marks in a dictionary.

students = {
"Ajay":78,
"Ravi":92,
"Neha":85,
"Aman":65
}

Write a program to:

* Find the student with highest marks.
* Find the student with lowest marks.

Sample Output:
Highest Marks : Ravi 92
Lowest Marks : Aman 65
"""
n=int(input("Enter number of students: "))
d={}
i=0
while i<n:
    name=input("Enter student name: ")
    marks=int(input("Enter marks: "))
    d[name]=marks
    i=i+1

first=list(d.keys())[0]
max=d[first]
min=d[first]
max_stu=first
min_stu=first
for x in d:
    if d[x]>max:
        max=d[x]
        max_stu=x
    if d[x]<min:
        min=d[x]
        min_stu=x
print("Heighest marks ",max_stu,max)
print("Lowest marks ",min_stu,min)


