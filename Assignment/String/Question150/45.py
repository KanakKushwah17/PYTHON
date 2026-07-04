"""
45Check whether a string starts/ends with another string. S = "apple pie", Prefix = "apple", Suffix = "pie" Start: True, End: True

"""
s=input("Enter a string: ")
suffix=input("Enter another string: ")
prefix=input("Enter another string: ")
word=[]
item=""
for i in s:
    if i!=" ":
        item=item+i
    else:
        word.append(item)
        item=""
word.append(item)

for i in range(len(word)):
    if word[i]==suffix:
       print("TRUE")
