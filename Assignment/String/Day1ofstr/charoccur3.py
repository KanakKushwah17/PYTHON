"""
3.
Character Occurrence Checker in Product Review

An e-commerce website wants to know how many times a particular character appears in a product review.

Input: Enter product review: this product is really good Enter character to check: o

Output: Character 'o' occurs: 4 times
"""
s=input("Enter string : ")
word = input("Enter letter : ")
count=0
for i in s:
    if i==word:
        count=count+1
print(count)
