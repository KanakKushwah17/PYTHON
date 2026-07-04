"""
33Find the longest word. S = "find the longest word" "longest"

"""

s= "find the longest word"
word=[]
item=""
for i in s:
    if i!=" ":
        item=item+i
    else:
        word.append(item)
        item=""
word.append(item)


store=""
longest=0
for item in word:
    count = 0
    for i in item:
        count=count+1
    if count>longest:
        longest=count
        store=item

print(store)








