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
cons=0
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i==' ':
        pass
    else:
        cons+=1

print("Total consonant ",cons)


