"""
60Append two strings but remove adjacent duplicates. S1="miss", S2="issippi" "misisipi"

"""

s1=input("Enter your first string: ")
s2=input("Enter your second string: ")

add=s1+s2
store=""
for i in range(len(add)):
    if add[i]!=add[i-1]:
        store=store+add[i]
print(store)


