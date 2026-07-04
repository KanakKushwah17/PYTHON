"""
35Find the first palindrome word. S = "this madam is here" "madam"

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

for i in word:
    if i[: :-1]==i:
        print(i)
        
