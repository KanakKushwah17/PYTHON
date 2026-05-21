"""
4.
Consonant Counter in Student Name Record

A school management system wants to count how many consonants are present in student names.

Input: Enter student name: Ajay Singh Thakur

Output: Total consonants: 11

NOTE:

Ignore case sensitivity (treat A and a same)
Consider only English alphabets for vowel/consonant counting
Vowels: A, E, I, O, U
"""
s=input("Enter student name: ").lower()
count=0
i=0
while i<len(s):
    if s[i].isalpha():
        if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
            pass
        else:
            count=count+1

    i=i+1
print("Total consonants: ",count)


