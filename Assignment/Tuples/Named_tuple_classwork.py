"""from collections import namedtuple
Student=namedtuple("Student",["Name","Age","city"])
s1=Student("John",23,"M")
print(s1.Name)
print(s1.Age)
print(s1.city)"""

"""from collections import namedtuple
Account=namedtuple("Account",["accno","holdername","balance"])
acc=int(input("Enter Account Number: "))
hn=input("Enter Holder Name: ")
bal=float(input("Enter Balance: "))
acc=Account(acc,hn,bal)
print(acc.accno)
print(acc.holdername)
print(acc.balance)"""

"""
from collections import namedtuple
Students=namedtuple("Students",["rollno","name","marks"])

n=int(input("Enter number of students: "))
students=[]
for i in range(n):
    r=int(input("Enter roll number: "))
    n=input("Enter Name: ")
    m=int(input("Enter Marks: "))
    #s=Students(r,n,m)
    students.append(Students(r,n,m))
#print(students)

for s in students:
    print(s)

#for s in students:
    #print(s.rollno)
    #print(s.name)
    #print(s.marks)
"""

#Underscore Fields
"""from collections import namedtuple
Students=namedtuple("Students",["rollno","name","marks"])
s1=Students(21,"john",22)
print(Students._fields)
print(s1._fields)
"""

#asdict()
"""from collections import namedtuple
Students=namedtuple("Students",["rollno","name","marks"])
s1=Students(21,"john",22)
print(Students._fields)
print(s1._asdict())
"""
"""from collections import namedtuple
Students=namedtuple("Students",["rollno","name","marks"])
s1=Students(21,"john",22)
print(Students._fields)
print(s1)
s2=s1._replace(marks=30)
print(s1)
print(s2)
print(id(s1))
print(id(s2))

"""

from collections import namedtuple
Students=namedtuple("Students",["rollno","name","marks"])
Data=Students(21,"john",22)
s1=Students._make(Data)
print(s1.rollno)
print(s1.name)
print(s1.marks)