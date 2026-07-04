"""76Find the longest common suffix among strings. Strings = ["baking", "making", "taking"] "king"

"""

s=input("Enter strings: ")
words=s.split()
words = words[::-1]
word=words[0]

res=""
for i in range(len(word)):
    found = 1
    for j in range(1,len(words)):
        w=words[j]
        if i<len(w):
            if w[i]!=word[i]:
                found=0
                break
        else:
            continue
    if found==1:
        res=res+word[i]
print(res)

