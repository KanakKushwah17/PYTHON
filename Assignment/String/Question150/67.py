"""
67Count how many times a substring appears. S = "abab", Sub = "ab" 2

"""
s=input("Enter string: ")
sub=input("Enter substring: ")

count=0
for i in range(len(s)):
    for j in range(i,len(s)):

        a=s[i:j+1]

        if sub==a:
            count+=1
print(count)
