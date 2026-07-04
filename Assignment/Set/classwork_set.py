"""s={1,2,3,4,2,11,22,33,44,44}
print(s)"""

"""s=set([33,44,44,22,11])
print(s)"""

"""s={10,20,30,40,30}
print(s)
#print(s[0])
for i in s:
    print(i)"""

"""s={10,20,30,40,30}
print(s)
s.add(90)
print(s)"""

"""s={10,20,30,40,30}
print(s)
s.update([3,4,2,5,5])
print(s)
"""

"""s={10,20,30,40,30}
print(s)
s.remove(30)
print(s)
"""
"""
s={10,20,30,40,30}
print(s)
s.discard(222)
print(s)
"""


"""s={10,20,30,40,30}
print(s)
s.pop()
print(s)"""

"""s={1,2,3,4,}
print(s)
s.clear()
print(s)"""

"""s1={10,20,30,40,30}
s2={30,40,50,60,70}
print(s1)
print(s2)
print(s1|s2)
print(s1.union(s2))
"""

"""s1={"hello","world"}
s2={"hello","world","kanak"}
print(s1)
print(s2)
print(s1.union(s2))
"""
"""s1={"hello","world"}
s2={"hello","world","kanak"}
print(s1)
print(s2)
print(s1.intersection(s2))"""


"""s1={10,20,30,40,30}
s2={30,40,50,60,70}
print(s1)
print(s2)
print(s1 & s2)
print(s1.intersection(s2))"""


"""
s1={10,20,30,40,30}
s2={30,40,50,60,70}
print(s1)
print(s2)
print(s1-s2)
print(s1.difference(s2))
"""

"""s1={10,20,30,40,30}
s2={30,40,50,60,70}
print(s1)
print(s2)
print(s1>=s2)
print(s1.issuperset(s2))"""


"""
s1={10,20,30,40,30}
s2={30,40,50,60,70}
print(s1)
print(s2)
print(s1<=s2)
print(s1.issubset(s2))
"""

"""s1={10,20,30,40,30}
s2={30,40,50,60,70}
print(s1.isdisjoint(s2))"""


"""
s1={1,2,3}
s2={5,6}
print(s1.isdisjoint(s2))"""


"""s1={1,2,3}
s2={3,4,5,6}
s1.intersection_update(s2)
s1&=s2
"""
"""
s1={1,2,3}
s2={3,4,5,6}
s1.difference_update(s2)
s1-=s2
print(s1)

s={1,2,3}
c={3,4,5,6}
s.symmetric_difference_update(c)
s^=c
print(s)"""

"""str=input("Enter string ")
s1=str.split()#list
print(s1)
u=set(s1)
print(u)

another=list(u)
print(another)"""

"""str=input("Enter string ")
u=set(str)
print(u)
if len(u)==len(str):
    print("No duplicates")
else:
    print("Duplicates")
"""
str=input("Enter string ")
u=set(str)
print(u)
repeat=0
if len(u)==len(str):
    print("No duplicates")
    repeat=1

else:
    print("Duplicates")
if repeat==1:
    print(u)

