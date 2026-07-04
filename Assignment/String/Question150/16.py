"""
16Count total occurrences of a character. S = "programming", Char = 'g' 2

"""
s=input("Enter string:")
char=input("Enter char:")
count=0
for i in s:
    if char==i:
        count+=1
print(count)