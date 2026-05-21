"""
1.Vowel Counter in Customer Feedback

 A company wants to analyze customer feedback messages by counting how many vowels are present in the feedback.

Input: Enter feedback message: Hello Customer Service

Output: Total vowels: 8
"""
msg=input("Enter feedback message: ")
count=0
for l in msg:
    if l=='a' or l=='e' or l=='i' or l=='o' or l=='u':
        count=count+1
print("Total vowels: ",count)
