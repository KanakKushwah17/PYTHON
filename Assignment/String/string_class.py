"""s1="deepika "
s2="Rashmika"
print(s1)
print(s2)


s1="""
"""
print(s1)
s2='''
hello world
How are you?'''
print(s2)"""

"""s1="deepika"
print(s1[0])
print(s1[3])
print(s1[-1])
print(s1[-2])
print(s1[-7])
"""
# syntax string

"""s1="hello world"
print(s1)
s2="hello world"
print(s2)
print(s1[6:14])
print(s1[6:11])
print(s1[14:15])
print(s1[:5])
print(s1[6:])
print(s1[1:10:2])
print(s1[1:10:3])
print(s1[: :2])
print(s1[-5:])
print(s1[-8:])
print(s1[:-2])"""

#reverse
"""s1="hello world"
print(s1[::-1])"""

#palindrome
"""s1=input("Enter the string:")
if s1==s1[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
"""

#String Iteration
"""s1="Welcome"
for ch in s1:
    chr(ch)
"""
"""s1="Welcome"
count=0
for ch in s1:
    count=count+1
print(count)"""

"""s1=input("Enter the string:")
i=0
while i<len(s1):
    print(i," ",s1[i])
    i=i+1"""

#Index based Iteration
"""str="welcome"
for i in range(len(str)):
    print(i," ",str[i])"""

#enumerate
"""str=input("Enter the string:")
for i ,ch in enumerate(str) :
    print(i," ",ch)"""

#immutable
"""str="Welcome"
str[1]="r"
print(str)"""

"""str="Welcome"
print(id(str))
str=str+"Home"
print(str)
print(id(str))"""

#iterning
"""a="welcome"
b="welcome"
print(id(a))
print(id(b))
a=a+"hello"
print(a)
print(id(a))"""

#deletion
"""a="welcome"
print(a)
del a[2]#error
del a
print(a)"""

# Check password
"""password= input("Enter the password:")
upper=0
lower=0
digit=0
space=0
special=0
i=0
while i<len(password):
    ch= password[i]
    if ch>='A' and ch<='Z':
        upper=1
    elif ch>='a' and ch<='z':
        lower=1
    elif ch>='0' and ch<='9':
        digit=1
    elif ch==" ":
        space=1
    else:
        special=1
    i=i+1
if len(password)>=8 and len(password)<=15 and upper == 1 and lower == 1 and digit == 1 and space == 0 and special ==1:
    print("Valid Password")
else:
    print("Invalid Password")"""

# Display string in forward and backward
"""str=input("Enter the string:")
n=len(str)
print(n)
i=0
while i<n:
    print(str[i],end="")
    i=i+1
print()
i=n-1
while i>=0:
    print(str[i],end="")
    i=i-1
print()
i=-1
while i>=-n:
    print(str[i],end="")
    i=i-1

for i in str:
    print(i)
print("Areee ye last he ")
for i in range(len(str)):
    print(str[i])
print("Kanak")
for i in range(n-1,-1,-1):
    print(str[i])
"""

#WAP to convert first character of every word into uppercase
"""print(ord("a"))
print(ord("1"))
print(ord("A"))

str=input("Enter the string:")
result=" "
i=0
while i<len(str):
    if i==0 or str[i-1]==" ":
        upper = ord(str[i])-32
        result = result + chr(upper)
    else:
        result = result + str[i]
    i=i+1
print(result)"""
"""
str=input("Enter the string:")
result=""
i=0
while i<len(str):
    if str[i]>="0" and str[i]<="2":
        if i==0 or str[i-3]==" ":
            upper = ord(str[i])-32
        else:
            result = result + str[i]
    else:
        result = result + str[i]
    i=i+1
print(result)"""

"""str=input("Enter the string:")
result=""
words=str.split()
for w in words:
    result = result + w.capitalize()+" "
print(result)
"""

#  WAP to check two strings are anagrams
"""s1=input("Enter the string:")
s2=input("Enter the string:")
if len(s1)==len(s2):
    if sorted(s1)==sorted(s2):
        print("Anagrams")
    else:
        print("Not Anagrams")
else:
    print("Not Anagrams")"""

"""s=input("Enter  the string ")
s1=""
s2=""
result=""
for x in s:
    if x.isalpha():
        s1=s1+x
    else:
       s2=s2+x
print(s1)
print(s2)
for x in sorted(s1):
    result=result+x
print(result)
for x in sorted(s2):
    result=result+x
print(result)"""

"""s=input("Enter the string")
result=""
for x in s:
    if x.isalpha():
        result=result+x
        previous=x
    else:
        result=result+previous*(int(x)-1)
print(result)"""

"""s=input("Enter the string")
result=""
for x in s:
    if x.isalpha():
        result=result+x
        previous=x
    else:
        newch=chr(ord(previous)+int(x))
        result=result+newch
print(result)  """

#write a program to reverse a string.
"""s=input("Enter the string ")
rev=""
i=len(s)-1
while i>=0:
    rev=rev+s[i]
    i=i-1
print(rev)"""

'''
s=input("Enter the string ")
rev=s[::-1]
print(rev)
'''
"""
s=input("enter the string ")
ls=s.split()
res=""
for i in range(len(ls)-1,-1,-1):
    res=res+ ls[i] + " "
print(res)
"""

"""
s=input("Enter the string ")
ls=s.split(" ")
print(" ".join(ls[::-1]))
"""

#write a program to reverse each word.
"""s=input("Enter the string ")
words=s.split()
i=0
while i<len(words):
    word=words[i]
    rev=""
    j=len(word)-1
    while j>=0:
        rev=rev+word[j]
        j=j-1
    print(rev,end=" ")
    i+=1   """

"""s=input("Enter the string ")
words=s.split()
for word in words:
    print(word[::-1],end=" ")"""

"""s=input("Enter the string ")
rev=s[::-1]
rev2=rev.split()
print(rev)
print(rev2)
print(" ".join(rev2[::-1]))"""

#27/05/2026
#REMOVE ELEMENT FROM LIST
#REMOVE()
"""a=[10,20,30,40,50]
print(a)
a.remove(10)
print(a)"""
"""a.remove(90)
print(a)#ERROR
"""

#POP
"""
a=[10,20,30,40,50]
a.pop()
print(a)
x=a.pop(1)
print(a)
a.pop(7)
print(x)
"""

#clear
"""a=[10,20,30,40,50]
print(a)
print(len(a))
a.clear()
print(a)
print(len(a))
"""
#del keyword
"""1.  a=[10,20,30,40,50]
print(a)
del a[1]
print(a)"""

"""
2. a=[10,20,30,40,50]
del a=[1:4]
print(a)
"""
"""
3. a=[10,20,30,40,50]
print(a)
del a
print(a)#ERROR
"""

#REMOVING ELEMENT WHILE ITERATING
"""a=[10,20,30,40,50]
for i in a:
    if i%2==0:
        a.remove(i)
print(a)"""

"""a=[10,20,30,40,50]
for i in a[ : ]:
    if i%2==0:
        a.remove(i)
    print(a)"""

"""a=[10,21,31,4,50]
for i in a[ : ]:
    if i%2==0:
        a.remove(i)
print(a)"""



#REMOVE Element based on user input
"""a=["kanak","avni","him","her"]
name=input("Enter your name:")
if name in a:
    a.remove(name)
else:
    print("name not found")
print(a)"""


"""a=["kanak","avni","him","her"]
b=a
name=input("Enter your name:")
if name in a:
    a.remove(name)
else:
    print("name not found")
print(a)
print(b)"""

#INDEX
"""a=["kanak","avni","him","her"]
print(a.index("him"))
print(a.count("him1"))
"""
#COUNT
"""a=["kanak","avni","him","her"]
print(a.count("him"))

b=[10,20,30,40,10]
print(b.count(10))"""


#SORT
"""a=["kanak","avni","him","her"]
a.sort()
b=[10,90,30,60,50]
b.sort()
print(a)
print(b)
"""
#rev sort
"""a=[10,20,30,40,50]
a.sort(reverse=True)
b=[10,90,30,60,50]
b.sort(reverse=True)
print(a)
print(b)"""

"""a=["kanak","avni","him","her"]
a.sort(key=len)
print(a)
"""
"""a=[10,-8,-7,3,2,8,4]
a.sort(key=abs)
print(a)
"""
"""
a=["kanak","avni","him","her"]
a.sort(key=str.lower))
print(a)"""

#SORTED
"""a=["kanak","avni","him","her"]
b=sorted(a)
print(a)
print(b)
"""

"""a=[19,35,60,27]
b=sorted(a)
print(a)
print(b)
"""


#Reverse
"""a=[10,11,5,7,3]
a.reverse()
print(a)"""

#copy()
"""a=[10,11,2,344,63]
b=a.copy()
print(a)
print(b)
a[0]=99
print(a)
print(b)
"""








