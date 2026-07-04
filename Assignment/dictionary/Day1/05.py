"""
5.

=========================================
WORD LENGTH GROUPING
====================

A content management system stores article tags.

tags = ["python","java","api","react","html","css"]

Write a program to:

* Group words according to their length.
* Store result in dictionary.

Sample Output:
{
3:['api','css'],
4:['java','html'],
5:['react'],
6:['python']
}

"""
tags=[]
n=int(input("Enter number of words: "))
i=0
while i<n:
    tag=input("Enter tags: ")
    tags.append(tag)
    i=i+1
d={}
for i in tags:
    l=len(i)
    if l in d:
        d[l].append(i)
    else:
        d[l]=[i]
print(d,end=" ")
