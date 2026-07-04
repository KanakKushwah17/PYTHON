"""
69Count how many times 'life' appears in a string. S = "life is life" 2

"""
s=input("Enter string: ")
sub="life"
word=[]
count=0
temp=""
for i in s:
    if i!=" ":
        temp=temp+i
    else:
        word.append(temp)
        temp=""
word.append(temp)

for i in word:
    if i==sub:
        count+=1
print(count)
