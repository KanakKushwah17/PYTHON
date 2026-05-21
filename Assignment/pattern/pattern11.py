"""
A
AB
ABC
ABCD
ABCDE
"""
n=input("Enter a number: ")
for i in range(1,int(n)+1):
    ch=65
    for j in range(1,i+1):
        print(chr(ch),end="")
        ch = ch + 1
    print()






