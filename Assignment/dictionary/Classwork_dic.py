#syntax
"""d={key1:value1,key2:value2}"""
"""
d={1:"kanak",2:"hello",3:"what",4:"are",5:"you",6:"doing"}
print(d)
d2=dict(a="abcd",b="xyz",c="BKL")
print(d2)
"""
"""student={
    "name":"mahesh",
    "age":18,
    "city":"Indore"
}
print(student)
print(student.get("name"))
print(student["city"])
print(student["age"])
print(student.get("city"))"""


"""d={}
n=int(input("Enter number of students : "))
i=0
while i<n:
    name=input("Enter student name :")
    marks=int(input("Enter student marks :"))
    d[name]=marks
    i=i+1
print("Name of student ","\t","% of marks")
for x in d:
    print(x,"\t",d[x])"""

"""d={1:"dipu",2:"rashmika"}
print(d)
d[3]="virat"
print(d)
d[1]="Him"
print(d)
del d[3]
print(d)
"""
"""d={1:"dipu",2:"rashmika",1:"virat"}
print(d)"""

"""d={1:"dipu",2:"rashmika",3:"dipu"}
print(d)"""

"""student={"name":"mahesh","age":18,"city":"Indore"}
print(student)
print(student.pop("name"))
print(student)
"""

"""student={"name":"mahesh","age":18,"city":"Indore",1:"hello"}
print(student)
print(student.pop(1))
print(student)
"""


"""student={"name":"mahesh","age":18,"city":"Indore"}
print(student)
print(student.popitem())
print(student)"""

"""student={"name":"mahesh","age":18,"city":"Indore"}
print(student)
while student:
    print(student.popitem())
"""
"""
student={"name":"mahesh","age":18,"city":"Indore",1:"hello"}
print(student)
del student["city"]
print(student)

del student[1]
print(student)"""

"""s={"name":"mahesh","age":18,"city":"Indore"}
print(s)
del s
"""

"""s={"name":"mahesh","age":18,"city":"Indore"}
print(s)
s.clear()
print(s)"""


"""student={"name":"mahesh","age":18,"city":"Indore"}
print(student)
print(student.keys())
print(list(student.keys()))
print(set(student.keys()))
"""
"""student={"name":"mahesh","age":18,"city":"Indore"}
print(student)
print(student.values())"""

"""student={"name":"mahesh","age":18,"city":"Indore"}
print(student)
print(student.items())
print(list(student.items()))

"""

"""student={"name":"mahesh","age":18,"city":"Indore"}
print(student)
for key ,value in student.items():
    print(key,":",value)
"""
"""
student={"name":"mahesh","age":18,"city":"Indore"}
print(student)
student.update({"salary":500})
student.update({"city":"chennai"})
print(student)"""
"""
student={"name":"mahesh","age":18,"city":"Indore"}
print(student)
s1=student.copy()
print(s1)
s1.update({"salary":400})
print(s1)
print(student)
s2=student
s2.update({"salary":400})#shallow copy
print(s1)"""

"""
student={"name":"mahesh","age":18,"city":"Indore","marks":[33,99]}
print(student)
s1=student.copy()
print(s1)
s1["marks"][0]=99
print(student)
print(s1)"""

"""import copy
student={"name":"mahesh","age":18,"city":"Indore","marks":[33,99]}
print(student)
s1=student.copy()
s2=copy.deepcopy(student)
print(s1)
s1["marks"][0]=99
print(student)
print(s1)"""

#Comprehension

"""
sq={}
for i in range(1,6):
    sq[i]=i*i
print(sq)"""


"""sq={i:i*i for i in range(1,6)}
print(sq)"""


"""se={i:i*i for i in range(1,11) if i%2==0}
print(se)

words={"dipu","rashmika","Kanak"}
d={word:len(word) for word in words }
print(d)
print(type(d))"""


"""num=[1,2,3,4,5,6,7,8,9]
r={x:"Even" if x%2==0 else "Odd" for x in num}
print(r)"""

"""keys=["name","age","city"]
values=["deepika",80,"Indore"]
d={keys[i]:values[i] for i in range(len(keys))}
print(d)"""

"""stu={
    101:{"name":"kanak","age":30},
    102:{"name":"deepika","age":40}
}
print(stu)
print(stu[101])
print(stu[102]["name"])"""

"""stu={
    101:{"name":"kanak","age":30},
    102:{"name":"deepika","age":40}
}
print(stu)
print(stu[101])
print(stu[102]["name"])
stu[103]={"name":"kanak","age":20}
print(stu)"""



"""
stu={
    101:{"name":"kanak","age":30},
    102:{"name":"deepika","age":40}
}
stu[103]={"name":"kanak","age":20}

for k,v in stu.items():
    print("ID",k)
    for k1,v1 in v.items():
        print(k1,"=",v1)"""

"""response={
"user":{
"id":101,
"profile":{"name":"dipu", "email":"d@gmail.com"}

}
}

print(response["user"]["profile"]["email"])  #d@gmail.com"""

"""d=eval(input("enter dictionary"))
print(type(d))
print(d)

a=eval(input("enter num "))
print(type(a))
print(a)

l=eval(input("enter list "))
print(type(l))
print(l)
"""

"""d=eval(input("enter dictionary"))
print(type(d))
print(d)

s=sum(d.values())
print(s)"""

"""n=int(input("enter number"))
d={}
for i in range(n):
    key=input("enter key")
    value=input("enter value")
    d[key]=value
print(d)
print(type(d))

s=sum(d.values())
print(s)
"""


"""word=input("Enter word")
d={}
for x in word:
    d[x]=d.get(x,0)+1
print(d)

for k,v in d.items():
    print(k,"occured",v,"items")"""

"""word=input("Enter word")
vowels={'a','e','i','o','u'}
d={}
for x in word:
    if x in vowels:
        d[x]=d.get(x,0)+1
print(d)

for k,v in d.items():
    print(k,"occured",v,"items")"""
"""
word=input("Enter word")
vowels={'a','e','i','o','u'}
d={}
for x in word:
    if x in vowels:
        d[x]=d.get(x,0)+1
print(d)

for k,v in sorted(d.items()):
    print(k,"occured",v,"items")"""

"""
logins=["kanak","shivani","Avni","Umesh","Bhavna","Bhoomika","Vanshika","VAnshika","Avni"]
c={}
for user in logins:
    c[user]=c.get(user,0)+1
print(c)"""
"""
words=["kanak","shivani","Avni","Umesh","Bhavna","Bhoomika","Vanshika","VAnshika","Avni"]
g={}
for w in words:
    l=len(w)
    if l not in g:
        g[l]=[]
    g[l].append(w)
print(g)"""

"""d1={"goa":5,"nepal":3,"delhi":8}
d2={"goa":5,"hyd":3,"delhi":8}

print(d1)
print(d2)

merged=d1.copy()
for k,v in d2.items():
    merged[k]=merged.get(k,0)+v
print(merged)
"""



