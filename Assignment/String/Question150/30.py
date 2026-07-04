"""
30Replace a word with another word. S = "old data", Old="old", New="new" "new data"

"""
s=input("enter word")
old=input("enter word")
new=input("enter new word")
rev=""
spl=s.split()
for i in spl:
    if i==old:
        rev=rev+new+" "
    else:
        rev=rev+i+" "
print(rev)
