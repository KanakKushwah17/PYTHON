"""
21Find the first non-repeating character. S = "aabbcde" c'

"""
s=input("enter string")
store=""

max=999
for i in s:
    count = 0
    for j in s:
        if i==j:
            count=count+1
    if count == 1:
        print(i)
        break



