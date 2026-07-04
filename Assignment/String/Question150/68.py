"""
68Count the sum of digits present in a string. S = "a1b2c3" 6 (1+2+3)

"""
s=input("Enter string: ")

sum=0

for i in s:

    if '0'<=i<='9':
        sum=sum+int(i)

print(sum)