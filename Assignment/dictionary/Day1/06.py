"""
6.
=========================================
MOBILE APP DOWNLOAD COUNTER
===========================

Downloads received from different cities:

cities = ["Indore","Bhopal","Indore","Pune","Delhi","Pune","Indore"]

Write a program to:

* Count downloads city-wise.
* Display city with maximum downloads.

Sample Output:
{'Indore':3,'Bhopal':1,'Pune':2,'Delhi':1}
Most Downloads : Indore

---
"""
cities = ["Indore","Bhopal","Indore","Pune","Delhi","Pune","Indore"]
# cities=[]
# n=int(input("Enter number of words: "))
# i=0
# while i<n:
#     city=input("Enter tags: ")
#     cities.append(city)
#     i=i+1


d={}
for i in cities:
    d[i]=d.get(i,0)+1

print(d)

