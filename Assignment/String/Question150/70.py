"""
70Compare the number of times 'the' and 'is' appear. S = "the cat is on the mat" the: 2, is: 1 (theis)

"""
s=input("Enter the string")
_is=0
_the=0
word=[]
temp=""
for i in s:
    if i!=" ":
        temp=temp+i
    else:
        word.append(temp)
        temp=""
word.append(temp)

for k in word:
    if k=="the":
        _the+=1
    if k=="is":
        _is+=1
print("is",_is,"the",_the)
