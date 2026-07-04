"""
27Find the last occurrence of a word. S = "Test this test", Word = "test" 15 (index)

"""
s=input("Enter string : ")
found=input("Enter word : ")
word = ""
start=0
for i in range(0,len(s)):
    if s[i] != " ":
        word = word + s[i]
        start = i
    else:
        word = ""
    if word==found:
        print(start)


