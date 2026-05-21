"""
8.
Mirror Difference Transaction Verification System
A multinational banking company processes thousands of daily transaction IDs. To detect suspicious patterns and validate system-generated IDs,
 the security software performs a Mirror Difference Verification Test.
For every entered transaction ID:

Reverse the digits of the transaction ID

Find the absolute difference between the original ID and the reversed ID


Count the total number of digits in the difference


Apply the following conditions using if-elif-else:

If the difference is 0, print Perfect Match


Else if the difference is divisible by 9, print Verified


Else print Rejected


Write a program to automate this verification process using loops and conditional statements.
Input:
4215
Output:
Reverse = 5124Difference = 909Digits = 3Verified
Input:
1221
Output:
Reverse = 1221Difference = 0Digits = 1Perfect Match
Input:
1234
Output:
Reverse = 4321Difference = 3087Digits = 4Verified


"""

digit=int(input("Enter the number :"))
temp=digit
rev=0
count=0

while digit>0:
    rem=digit%10
    rev=rev*10+rem
    digit=digit//10
print("Reverse : ",rev)

diff=abs(temp-rev)
print("Difference : ",diff) 
diff2=diff
while diff!=0:
    diff%10
    count=count+1
    diff=diff//10
if diff2 == 0:
    count = 1

print("Digits :", count)

if diff2==0:
    print("Perfect Match ")
elif diff2%9==0:
    print("Verified")
else:
    print("Rejected ")


