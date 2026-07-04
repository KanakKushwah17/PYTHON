"""
74Find the longest substring without repeating characters. S = "abcabcbb" "abc"

"""
s=input("Enter string:")
rev=""
for i in range(len(s)):
    for j in range(len(s)):
        if s[i]==s[j]:
            pass
        else: 
            rev=rev+s[i]+""
print(rev)