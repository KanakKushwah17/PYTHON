#WAP TO SEPERATE EVEN AND ODD
"""n=int(input("Enter number"))
arr=[]
for i in range(n):
    x=int(input("Enter element "))
    arr.append(x)
print(arr)
even=[]
odd=[]
for i in arr:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)"""

#WAP TO FIND COMMON ELEMENT BETWEEN LIST
"""s1=int(input("Enter a string"))
s2=int(input("Enter another string"))


arr1=[]
for i in range(s1):
    x=int(input("Enter element "))
    arr1.append(x)
print(arr1)


arr2=[]
for i in range(s2):
    x=int(input("Enter element "))
    arr2.append(x)
print(arr2)

common=[]
for i in arr1:
    if i in arr2:
        if i%2==0 and i>10:
            common.append(i)

print(common)"""

"""a=[1,2,3]
b=[3,4,5,]
merged=a+b
print(merged)
result=[]
for i in merged:
    if i not in result:
        result.append(i)
print(result)
"""

"""a=[1,2,3,4,5,6]
a.reverse()
print(a)"""

"""a=[1,2,3,4,5,6]
b=a[: :-1]
print(b)
print(a)"""

"""a=[1,2,3,4,5,6]
rev=[]
for i in a:
    rev=[i]+rev
print(rev)
print(a)"""

"""a=[1,0,3,0,5,6]
non_zero=[]
zero=[]

for i in a:
    if i==0:
        zero.append(i)
    else:
        non_zero.append(i)
merge=non_zero+zero
print(merge)"""
"""
n=int(input("Enter number"))
arr=[]
for i in range(n):
    x=int(input("Enter element "))
    arr.append(x)
print(arr)

peakindex=-1
for i in range(n):
    if i==0 and arr[i]>=arr[i+1]:
        peakindex=i
        break
    elif i==n-1:
        if arr[i]>arr[i-1]:
            peakindex=i
            break
    else:
        if arr[i]>=arr[i-1] and arr[i]<=arr[i+1]:
            peakindex=i
            break
if peakindex!=-1:
    print("peak element is ",peakindex,"and value is ",arr[peakindex])
else:
    print("No peak element found")

"""
"""n=int(input("Enter number"))
arr=[]
for i in range(n):
    x=int(input("Enter element "))
    arr.append(x)
print(arr)

sum=0
for i in range(n):
    isleader=True
    for j in range(i+1,n):
        if arr[i]<=arr[j]:
            isleader=False
            break
    if isleader:
        sum=sum+arr[i]
print(sum)

"""
"""n=int(input("Enter number"))
arr=[]
for i in range(n):
    x=int(input("Enter element "))
    arr.append(x)
print(arr)
neg=[]
pos=[]
for i in range(n):
    if arr[i]<0:
        neg.append(arr[i])
    else:
        pos.append(arr[i])
merge=pos+neg
print(merge)"""

"""n=int(input("Enter number"))
arr=[]
for i in range(n):
    x=int(input("Enter element "))
    arr.append(x)
print(arr)
last=arr[n-1]
i=n-1
while i>0:
    arr[i]=arr[i-1]
    i=i-1
arr[0]=last
print(arr)
"""
#LIST COMPREHENSIVE
"""a=[1,2,3,4,5]
b=[]
for i in a:
    b.append(i*2)
print(b)"""

"""a=[1,2,3,4,5]
b=[i*2 for i in a]
print(b)
"""
"""[expression for in iteration]"""

"""a=[1,2,3,4,5,6,7,8]
b=[i for i in a if i%2==0 and i>3]
print(b)
"""


"""
a=[1,2,3,4,5,6,7,8]
b=["Even " if i%2==0 else "Odd " for i in a]
print(b)
"""

"""a=["kanak ", "varun","kriti"]
b=[len(i) for i in a]
print(b)
"""

"""a=["kanak ", "varun","kriti"]
b=[i for i in a if len(i)>3]
print(b)"""

"""
a=["kanak ", "varun","kriti"]
b=[i.upper() for i in a ]
print(b)"""


"""a=[11,2,3,4,5,6]
b=[i*10 if i%2==0 else i for i in a]
print(b)"""


"""a=[1,2,[3,4],5,6]
print(a)
print(a[0])
print(a[2])
print(a[2][1])"""