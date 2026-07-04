"""
3.

=========================================
WEBSITE PAGE VISIT TRACKER
==========================

A website records page visits.

pages = ["Home","About","Home","Contact","Home","About"]

Write a program to:

* Count visits of each page using a dictionary.
* Display page name and visit count.

Sample Output:
Home visited 3 times
About visited 2 times
Contact visited 1 time

---
"""
n=int(input("Enter number of pages: "))
page=[]
i=0
while i<n:
    pname=input("Enter page name: ")
    page.append(pname)
    i=i+1
d={}
for x in page:
    if x in d:
        d[x]=d[x]+1
    else:
        d[x]=1

for k in d:
    print(k, "Visited ",d[k]," times")
