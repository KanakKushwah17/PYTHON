"""str=input("Enter a string")
n=len(str)
print(n)
for i in str:
    print(i)
    print("Areee ye last he")
    for i in range(len(str)):
        print(str[i])
        print("kanak")
    for i in range(n-1,-1,-1):
        print(str[i])"""


"""str=input("Enter a string")
result=" "
i=0
while i<len(str):
    if str[i]>="a" and str[i]<="z":
        if i==0 or str[i-1]==" ":
            upper=ord(str[i])-32
            result+=chr(upper)
        else:
            result+=str[i]
    else:
        result+=str[i]
    i=i+1
print(result)
"""
"""str=input("Enter a string")
result=""
i=0
while i<len(str):
    if i==0 or str[i-1]==" ":
        upper=ord(str[i])-32
        result+=chr(upper)
    else:
        result+=str[i]
    i=i+1
print(result)"""

"""
s1=input("Enter a string")
s2=input("Enter another string")
if len(s1)==len(s2):
    if sorted(s1)==sorted(s2):
        print("Anagram")
    else:
        print("Not Anagaram")
else:
    print("Not Anagram")"""



s1=input("Enter a string")
s2=input("Enter another string")
if len (s1)!=len(s2):
    print("Not Anagram")
else:
    f=1
    for ch in s1:
        if s1.count(ch)!=s2.count(ch):
            f=0
            break
        if f==1:
            print("Anagram")
        else:
            print("Not Anagram")