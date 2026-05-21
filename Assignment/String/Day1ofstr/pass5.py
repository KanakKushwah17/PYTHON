"""
5.
Advanced Password Security Checker

A cyber security company wants to verify whether employee passwords are highly secure before giving system access.

Conditions: Password must:

Start with an uppercase letter
End with a digit
Contain at least 2 digits
Contain at least 1 special character (@ # $ % & *)
Must not contain spaces
Length should be between 8 and 15 characters

Input: Enter password: Python@45

Output: Secure Password

"""
password=input("Enter password: ")
an=0
digit=0
special=0
space=0
for i in range(len(password)):
    ch=password[i]
    if ch>='0' and ch<='9':
        digit+=1
    elif ch>='a' and ch<='z':
        an=an+1
    elif ch == '@' or ch == '#' or ch == '$' or ch == '%' or ch == '&' or ch == '*':
        special += 1
    elif ch == " ":
        space += 1
if ((password[0] >= 'A' and password[0] <= 'Z') and
    (password[len(password)-1] >= '0' and password[len(password)-1] <= '9') and
    digit >= 2 and
    special >= 1 and
    space == 0 and
    len(password) >= 8 and len(password) <= 15):

    print("Secure Password")

else:
    print("Invalid Password")


