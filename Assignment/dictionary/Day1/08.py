"""
8.
=========================================
LIBRARY BOOK ISSUE TRACKER
==========================

A library records issued books.

books = [
"Python",
"Java",
"Python",
"C++",
"Java",
"Python"
]

Write a program to:

* Count how many times each book was issued.

Sample Output:
{
'Python':3,
'Java':2,
'C++':1
}
"""
tags=[]
n=int(input("Enter number of words: "))
i=0
while i<n:
    tag=input("Enter tags: ")
    tags.append(tag)
    i=i+1

count=0
d={}
for i in tags:
    d[i]=d.get(i,0)+1

print(d)