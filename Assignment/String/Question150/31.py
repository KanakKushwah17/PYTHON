"""
31Remove duplicate words. S = "the cat and the dog" "the cat and dog"

"""

s=input("Enter string :")
snew=s.split()
word=""
for i in snew:
    if i not in word:
        word=word+i+" "
print(word)