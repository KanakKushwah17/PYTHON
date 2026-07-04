"""
25Count total words in a string. S = "This is a test" 4

"""
s=input("Enter string")
count=0
sspl=s.split()
for i in sspl:
    count=count+1
print(count)