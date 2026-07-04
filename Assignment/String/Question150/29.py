"""
29Remove occurrences of a word. S = "a test b test c", Word = "test", Remove All "a b c"

"""
s=input("Enter a word: ")
word=input("Enter a word: ")
spl=s.split()
rev=""
for i in spl:
    if i!=word:
        rev=rev+i+" "
print("Remove all ",rev)
