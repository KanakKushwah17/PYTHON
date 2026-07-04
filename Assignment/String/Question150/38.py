"""
38Reverse words without split(). S = "a b c" "c b a"

"""
s=input("Enter the string")
rev=""

for i in range(len(s)):
         rev=rev+s[::-1]
         break
print(rev)