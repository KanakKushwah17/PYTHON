"""
61Count total alphabets, digits, and special characters. S = "a1b!c2" Alphabets: 3, Digits: 2, Special: 1

"""
s=input("Enter string: ")

alpha=0
digit=0
special=0

for i in s:

    if 'a'<=i<='z' or 'A'<=i<='Z':
        alpha=alpha+1

    elif '0'<=i<='9':
        digit=digit+1

    else:
        special=special+1

print("Alphabets:",alpha)
print("Digits:",digit)
print("Special:",special)