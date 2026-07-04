"""
81Generate a hash code or UUID. S = "test" Hash: 3556498 (Example hash code)

"""
s=input("Enter a string: ")
hash=0
for i in s:
    hash=int(ord(i)+23)
    print(hash+2,end="")