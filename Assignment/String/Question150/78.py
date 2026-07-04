"""
78Find the longest mirror-image substring at both ends. S = "aabccbaa" "aab"

"""
s=input("Enter strings: ")

found=0
rev=""
for i in range(1,len(s)+1):
    prefix=s[:i]
    suffix=s[-i:]
    if prefix==suffix:
        rev+=prefix

print(rev)

