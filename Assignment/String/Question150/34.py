"""
34Find the shortest word. S = "find the shortest word" "the"

"""
s=input("Enter a string")
word=[]
temp=""
for i in s:
    if i!=" ":
        temp+=i
    else:
        word.append(temp)
        temp=""
word.append(temp)
print(word)

store=""
min=len(word[0])
for i in word:
    count=0
    for j in i:
        count+=1
    if count<min:
        min=count
        store=i
print(store)