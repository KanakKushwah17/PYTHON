"""
6.
Data Validation System – Character Identifier
A system needs to validate user input characters.
If the input is:
Alphabet → display "Alphabet"
Digit → display "Digit"
Otherwise → display "Special Character"
Write a program using inline if to classify the character.
"""
ch=input("Enter a character :")
char= "Alphabet " if   ('a' <= ch <= 'z' or 'A' <= ch <= 'Z') else "Digit " if ('0'<=ch<='9') else "Special Character"
print(char)