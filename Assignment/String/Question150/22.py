"""
22Find the last repeating character. S = "abracadabra" r'
"""
s=input("enter string")
store=""

max=0
for i in s:
    count = 0
    for j in s:
        if i==j:
            count=count+1
    if count> 1:
        store=i
print(store)
