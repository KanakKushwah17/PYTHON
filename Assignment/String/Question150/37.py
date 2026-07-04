"""
37Reverse each word. S = "cat dog" "tac god"

"""

s=input("Enter the string")
rev=""
word=s.split()
for i in word:
         rev=rev+i[::-1]+" "
print(rev)