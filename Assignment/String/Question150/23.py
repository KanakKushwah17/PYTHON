"""
23Print all characters that occur exactly twice. S = "aabbcdee" b', 'e'

"""
s=input("Enter a string")
for i in s:
    count=0
    for j in s:
        if i==j:
            count=count+1
    if count==2:
        print(i)