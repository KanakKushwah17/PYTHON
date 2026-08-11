"""
26Find the first occurrence of a word. S = "Test this test", Word = "test" 10 (index)

"""

s = "Test this test"
found = "test"
word=[]
temp=""

for i in s:
    if i!=" ":
        temp=temp+i
    else:
        word.append(temp)
        temp=""
word.append(temp)
print(word)

index=0
for item in word:
    if item == found:
        print(index)
        break
    index += len(item) + 1
