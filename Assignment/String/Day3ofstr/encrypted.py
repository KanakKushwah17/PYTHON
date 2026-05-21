"""
Instant Messaging Word Encryption System

A messaging application wants to temporarily encrypt messages during
transmission. The encryption rule is to reverse every word individually
while keeping the word positions unchanged.

Input: Enter message: java is powerful

Output: Encrypted Message: avaj si lufrewop
"""
msg = input("Enter message: ")

words = msg.split()
result = ""

for i in words:
    rev = i[::-1]
    result = result + rev + " "

print("Encrypted Message:", result.strip())