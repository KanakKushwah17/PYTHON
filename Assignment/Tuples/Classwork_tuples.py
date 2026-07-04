"""t=(1,2,3)
print(t)
t1=1,2,3
print(t1)"""

#tuple constructor list
"""t=tuple([1,2,3])
print(t)
print(type(t))"""

"""
t=(10)
print(t)
print(type(t))

t1=(10,20,30)
print(t1)
print(type(t1))"""


#Accessing tuple element
"""t=(10,20,30)
print(t[0])
print(t[-1])
print(t[1:3])

t=(10,20,30)
t[0]=99
print(t)"""
"""
t=([10,20],30)
print(id(t)) 
print(type(t))
t[0].append(4)
print(t)
"""
"""#Packing
t=10,20,30
print(t)

#Unpacking
a,b,c=(10,20,30)
print(a,b,c)
"""
"""a,*b,c= (10,20,30,40,50)
print(a,b,c)"""

#Method in tuple
"""t=(10,20,30,40,50)
print(t)
print(t.count(10))"""

"""t=(10,20,30,40,50)
print(t)
print(t.index(30))
print(max(t))
print(min(t))
print(sum(t))"""

#Iterating tuple
#direct
"""t=(10,20,30,40,50)
print(t)
for i in t:
    print(i)"""
#Index
"""t=(10,20,30,40,50)
print(t)
for i in range(len(t)):
    print(t[i])"""

#tuple concatnation
"""t=(10,20,30,40,50)
t2=(60,70,80,90,100)
print(t+t2)
"""

"""t1=(10,20,30,40,50)
print(t1*3)"""

"""t1=((10,20),(30,40))
print(t1)
print(t1[0])
print(t1[1])
print(t1[0][1])"""

"""
id=int(input("Enter your ID:"))
name=input("Enter your name:")
salary=int(input("Enter your salary:"))
employee=(id,name,salary)
print("Employee details :")
print("ID:",employee[0])
print("Name:",employee[1])
print("Salary:",employee[2])
"""
"""
t=(10,20,30,40,50)
print(20 in t)
print(60 not in t)
"""

"""t1=(1,2,8)
t2=(1,2,4)
print(t1<t2)
"""
#del
"""
t1=(1,2,8)
del t1
"""

#tuple convert into list
"""
t1=(1,56,8)
print(t1)
l=list(t1)
print(l)

print(sorted(t1))
"""

"""
import sys
t1=("abc","def","ghi")
print(t1)
 
print(sys.getsizeof(t1))

t1=("abc","def","ghi")
print(t1)
print(sys.getsizeof(t1))
"""

"""
import sys
t1 = ("abc", "xyz", "www")
print(t1)
print(sys.getsizeof(t1))       # Size of the tuple which it is actually taking

t2 = ["abc", "xyz", "www"]
print(t2)
print(sys.getsizeof(t2))
"""



