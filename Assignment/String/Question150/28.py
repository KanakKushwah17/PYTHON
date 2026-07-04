"""
28Count occurrences of a word. S = "word word other word", Word = "word" 3

"""
s=input("Enter string : ")
snew=s.split()
word=input("Enter word : ")
count=0

for i in snew:
    if i==word:
        count=count+1
print(count)
