"""
3. Smart Scholarship Allocation System

A scholarship is provided based on marks, family income, and category.

If marks are 85 or above, then check income. If income is less than or equal to 300000, then check category. If category is not general, give Full Scholarship; otherwise give 75% Scholarship. If income is above 300000, give 50% Scholarship.

If marks are between 70 and 84, then check income. If income is less than or equal to 200000, give 50% Scholarship; otherwise give 25% Scholarship.

If marks are below 70, no scholarship is given.

Input:
Marks = 88
Income = 250000
Category = OBC

Output:
Scholarship = Full Scholarship
"""
marks = int(input("Enter Marks : "))
Income = int(input("Enter Income : "))
category = input("Enter general/obc/st/sc : ").lower()

if marks>=85:
    if Income<=300000:
        if category != "general ":
            print("Full Scolorship ")
        else:
            print("75% Scolorship ")
    else:
        print("50% scolorship ")
else:
    if marks>=70 and marks<=84:
        if Income<=200000:
            printf("50% scolorship")
        else:
            print("25% scolorship")
    else: 
        print("No scolorship")