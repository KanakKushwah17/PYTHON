#Using square bracket
"""l1=[10,"brackets",12.5]#list of mixed data
l2=[10,20,30]#list of integer
print(l1)
print(l2)
print(dir(l1))
"""
from Assignment.loops import unique

#create a list
"""
l=list("Welcome ")
print(l)
l2=list((12,14,"deepika"))
print(l2)
"""

#list with repeated item
"""l=[2]*5
print(l)
l2=["deepika",4]*5
print(l2)
"""

"""l=[10,20,30,40,50]
print(l[0])
print(l[-1])
print(l[1:4])"""

#Accessing using loop
# using for
""" 
 l=[10,20,30,40,50]
for i in l:
    print(i)
"""
#using while
"""
l=[10,20,30,40,50]
i=0
while i<len(l):
    print(l[i])
    i=i+1
"""
#Accessing using slicing
"""
l=[10,20,30,40,50]
print(l[:3])
print(l[2:])
print(l[::2])
"""

#Adding elements to the list
#append method
"""l=[10,20,30,40,50]
l.append(60)
print(l)

#Insert method
l=[10,20,30,40,50]
l.insert(1,99)
print(l)

l2=[10,20,30,40,50]
l2.insert(len(l),99)
print(l2)

l3=[10,20,30,40,50]
l3.insert(-1,99)
print(l3)
"""
"""a=[10,20,30,40,50]
a.insert(-10,9999)
a.insert(10,7777)
print(a)
print(a.index(9999))
print(a.index(7777))
"""
#Extend()
"""a=[10,20,30,40,50]
b=[60,70]
a.extend(b)
print(a)"""

"""a=[10,20,30]
b=[60,70]
a.extend(b)
print(a)
print(b)
"""
#append
"""a=[10,20,30]
a.append("hello")
a.extend("world")
print(a)"""

#COMPARING LIST OBJECT
"""a=["deepika","kanak","Avni"]
b=["deepika","kanak","Avni"]
c=["DEEPIKA","KANAK","AVNI"]
print(a==b)
print(a==c)
print(a!=c)
print(a is b )
print(id(a[0]))
print(id(b[0]))
print(a[0] is b[0])

d=[10,20,30]
e=[10,20,30]
print(d[0] is e[0])

"""
#UPDATING ELEMENTS INTO THE LIST
"""a=[10,20,30,40]
print(id(a))
a[1]=100
print(a)
print(id(a))"""

"""a=[10,20,30,40]
a[-1]=100
a[-10]=500
print(a)
"""

#UPDATING ELEMENTS USING SLICING
"""a=[10,20,30,40,50]
a[1:3]=[200,300]
print(a)"""

"""
a=[10,20,30,40,50]
a[1:4]=[10,20]
"""

#UPDATE ENTIRE LIST USING LOOPS
"""a=[1,2,3,4,5,6,7,8,9]
for i in range(len(a)):
    a[i]=a[i]*2
print(a)
"""
"""a=[1,2,3,4,5,6,7,8,9]
i=0
while i<len(a):
    a[i]=a[i]*2
    i=i+1
print(a)"""

#UPDATING ELEMENT BASED ON USER INPUT
"""marks=[80,90,70]
index=int(input("enter the index"))
value=int(input("enter the value"))
marks[index]=value
print(marks)"""

"""students=["cat","dog","bat"]
marks=[40,50,60]
name=input("enter your name")
if name in students:
    index=students.index(name)
    newmarks=int(input("enter your marks"))
    marks[index]=newmarks
    print(marks)
else:
    print("your name is not in the list")"""

#Even Index add
"""print("Enter the number of element ")
n=int(input())
arr=[]
for i in range(n):
    x=int(input("Enter element "))
    arr.append(i)
print(arr)
while i<len(arr):
    sum=sum+arr[i]
    i=i+2
print(sum)"""

#EVEN element add
"""print("Enter the number of element ")
n=int(input())
arr=[]
for i in range(n):
    x=int(input("Enter element "))
    arr.append(x)
print(arr)
sum=0
for i in range(n):
    if arr[i]%2==0:
        sum=sum+arr[i]
print(sum)
"""
#ERROR IN WHILE
"""print("Enter the number of element ")
n=int(input())
arr=[]
for i in range(n):
    x=int(input("Enter element "))
    arr.append(x)
print(arr)
sum=0
while i<len(arr):
    if arr[i]%2==0:
        sum=sum+arr[i]
    i=i+2
print(sum)"""

#WAP TO FIND MAX ELEMENT ARRAY
"""print("Enter the number of element ")
n=int(input())
arr=[]
for i in range(n):
    x=int(input("Enter element "))
    arr.append(x)
print(arr)
max=0
for i in range(n):
    if arr[i]>max:
        max=arr[i]
    i=i+1
print(max)"""

"""print("Enter the number of element ")
n=int(input())
arr=[]
for i in range(n):
    x=int(input("Enter element "))
    arr.append(x)
print(arr)
max=0
for i in arr:
    if i>max:
        max=i
    i=i+1
print(max)"""

"""print("Enter the number of element ")
n=int(input())
arr=[]
for i in range(n):
    x=int(input("Enter element "))
    arr.append(x)
print(arr)
max=9
for i in arr:
    if i<max:
        max=i
    i=i+1
print(max)
"""
"""print("Enter the number of element ")
n=int(input())
arr=[]
for i in range(n):
    x=int(input("Enter element "))
    arr.append(x)
print(arr)
visit=[]
for i in arr:
    if i not in visit:
        visit.append(i)
print(visit)"""

"""print("Enter the number of element ")
n=int(input())
arr=[]
for i in range(n):
    x=int(input("Enter element "))
    arr.append(x)
print(arr)
unique=[]
for i in range(len(arr)):
    if arr[i] not in unique:
        unique.append(arr[i])
print(unique)

"""

"""n=int(input("Enter the number of element"))
arr=[]
for i in range(n):
    x=int(input("Enter element "))   #ERROR
    arr.append(x)
print(arr)

for i in arr:
    count = 0
    for j in arr:
        if i==j :
            count=count+1
    if count>1:
        arr.remove(i)
print(arr)
"""
"""n=int(input("Enter the number of element"))
arr=[]
for i in range(n):
    x=int(input("Enter element "))
    arr.append(x)
print(arr)
unique=[]
for i in range(len(arr)):
    if arr[i] not in unique:
        unique.append(arr[i])
print(unique)
arr.sort()
print(arr[-2])
"""


