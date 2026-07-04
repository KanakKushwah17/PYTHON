"""
62Count vowels and consonants. S = "apple" Vowels: 2, Consonants: 3

"""
s=input("Enter string: ")

alpha=0
vowels=0

for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        vowels=vowels+1
    else:
        alpha=alpha+1
print("Alphabets:",alpha)
print("vowels:",vowels)
