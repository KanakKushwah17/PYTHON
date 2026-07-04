"""
58Rotate characters left by 2 positions. S = "abcde" "cdeab"

"""
s=input("Enter a string : ")
pos=int(input("Enter a position : "))
new=""
for j in range(len(s)-pos,len(s)):
    new=new+s[j]
for i in range((len(s)-pos)):
    new=new+s[i]

print(new)

