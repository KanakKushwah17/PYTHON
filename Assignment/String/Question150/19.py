"""
19Find the highest frequency character. S = "abracadabra" a'
"""
s=input("Enter a string")
max=0
new=""
for i in s:
    count=0
    for j in s:
        if i==j:
            count=count+1
        if max<count:
            max=count
        new=i
print(new)


