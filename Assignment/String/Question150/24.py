"""
24Check if all characters in a string are unique. S1 = "abc", S2 = "abca" S1: True, S2: False

"""

s=input("Enter a string: ").lower()

flag=True
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i]==s[j]:
            flag=False

print(flag)







