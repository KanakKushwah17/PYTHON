"""
1.
Email Username Validator

A company wants to check whether an employee email username is valid before creating an official account.

Conditions:
- Username should start with a letter
- Username can contain letters, digits, underscore (_)
- No spaces allowed
- Length should be between 5 and 12 characters

Input:
Enter username: ajay_123

Output:
Valid Username

"""
user=input("Enter username: ")

valid=False
underscore=0

if ((user[0]>='A' and user[0]<='Z') or (user[0]>='a' and user[0]<='z')):

    if len(user)>=5 and len(user)<=12:

        valid=True

        for i in range(len(user)):

            if ((user[i]>='A' and user[i]<='Z') or
                (user[i]>='a' and user[i]<='z') or
                (user[i]>='0' and user[i]<='9') or
                user[i]=='_'):

                if user[i]=='_':
                    underscore=1

            else:
                valid=False

if valid==True and underscore==1:
    print("Valid Username")
else:
    print("Invalid Username")