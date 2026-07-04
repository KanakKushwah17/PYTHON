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


for item in word:
    if item== found:
        print(item)
