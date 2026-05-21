"""
2. Hospital Emergency Priority System

A hospital assigns treatment priority based on age, severity, and insurance.

If severity is critical, then check age. If age is 60 or above, assign Immediate ICU; otherwise assign Emergency Ward.

If severity is moderate, then check insurance. If insured, assign Priority Treatment; otherwise assign General Queue.

If severity is low, then check age. If age is less than 10, assign Pediatric Priority; otherwise assign Wait.

Input:
Age = 65
Severity = critical
Insurance = yes

Output:
Treatment = Immediate ICU
"""
Age = int(input("Enter Age : "))
Severity = input("Enter ( critical/moderate/low ) : ").lower()
Insurance = input("Enter yes/No: ").lower()


if Severity=="critical":
    if Age>=60:
        print("Imediate ICU ")
    else:
        print("Emergency Ward")
if Severity=="Moderate":
     if Insurance=="yes":
         print("priority treatment ")
     else:
         print("General queue")
if Severity=="low":
     if Age<10:
         print("Pediatric Priority ")
     else:
         print("assign wait")

