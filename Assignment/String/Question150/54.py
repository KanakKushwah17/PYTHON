"""
54Replace duplicate chars with '$'. S = "hello" "he$lo"

"""
s=input("Enter a string ")
store=""
for i in s:
    count=0
    for j in s:
        if i==j:
            count+=1
    if count>1:
        store=store+"#"
    else:
        store=store+i
print(store)
