"""
7.
=========================================
ONLINE EXAM RESULT SYSTEM
=========================

Store student marks in a dictionary.

results = {
"Ajay":88,
"Ravi":45,
"Neha":76,
"Aman":39
}

Write a program to:

* Display names of students who passed.
  (Passing Marks = 50)

Sample Output:
Ajay
Neha
Ravi
"""
n=int(input("Enter number of students:"))
d={}
for i in range(n):
    keys=input("Enter name for student ")
    values = int(input("Enter marks for student "))
    d[keys]=values
print(d)

print("names of students who passed ")
for k,v in d.items():
    if v >50:
        print(k,v)

