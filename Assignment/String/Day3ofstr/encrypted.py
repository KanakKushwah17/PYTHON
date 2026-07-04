"""
Instant Messaging Word Encryption System

A messaging application wants to temporarily encrypt messages during
transmission. The encryption rule is to reverse every word individually
while keeping the word positions unchanged.

Input: Enter message: java is powerful

Output: Encrypted Message: avaj si lufrewop
"""
msg = input("Enter message: ")
word=msg.split()
res=""
for i in word:
    rev=i[: : -1]
    res+=rev+ " "
print("Encrypted message : ",res)


