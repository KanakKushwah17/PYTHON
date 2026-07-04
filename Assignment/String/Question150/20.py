"""
20Find the lowest frequency character. S = "aabbcde" c', 'd', 'e' (any one or all)

"""
s=input("Enter a string")
min=999999999999999999999999
new=""
for i in s:
    count=0
    for j in s:
        if i==j:
            count=count+1
        if min>count:
            min=count
        new=i
print(new)
