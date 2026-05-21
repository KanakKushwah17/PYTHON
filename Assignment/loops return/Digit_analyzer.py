"""
1.
Digit Frequency Balance Analyzer

A data security system analyzes numeric IDs to check digit distribution patterns.

For a given number, the system evaluates how frequently each digit appears.

Write a program to:

Count how many times each digit appears in the number
Display only the digits that appear more than once
Find the total count of repeated digits
Find the digit with maximum frequency
If no digit repeats, print Unique Number
If at least one digit repeats, print Repeated Pattern Detected

Use loops wherever required.

Input:
1223451

Output:
Repeated Digits: 1 2
Total Repeated Count = 4
Max Frequency Digit = 1
Repeated Pattern Detected
"""
n=int(input("Enter Number:"))
one,two,three,four,five,six,seven,eight,nine,zero,digit,count=0,0,0,0,0,0,0,0,0,0,0,0
while n>0:
    rem=n%10
    if rem==1:
        one = one+1
        if one>=2:
            digit = one
            print("Repeated Digits: 1")
    elif rem==2:
        two = two+1
        if two >= 2:
            digit = two
            print("Repeated Digits: 2")
    elif rem==3:
        three = three+1
        if three >= 2:
            digit=three
            print("Repeated Digits: 3")
    elif rem==4:
        four = four+1
        if four >= 2:
            digit=four
            print("Repeated Digits: 4")
    elif rem==5:
        five = five+1
        if five >= 2:
            digit=five
            print("Repeated Digits: 5")
    elif rem==6:
        six = six+1
        if six >= 2:
            digit=six
            print("Repeated Digits: 6")
    elif rem==7:
        seven = seven+1
        if seven >= 2:
            digit=seven
            print("Repeated Digits: 7")
    elif rem==8:
        eight = eight+1
        if eight >= 2:
            digit=eight
            print("Repeated Digits: 8")
    elif rem==9:
        nine = nine+1
        if nine >= 2:
            digit=nine
            print("Repeated Digits: 9")
    else:
        zero=zero+1
        if nine >= 2:
            digit=zero
            print("Repeated Digits: 0")
    if digit>1:

        print("Total Repeated Count = ",digit)
    n=n//10


