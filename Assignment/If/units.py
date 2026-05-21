"""
3. A smart electricity monitoring system categorizes usage levels for better energy management. 
The system should take the number of units consumed as input. If the units are greater than or equal to 100, then check further.
 If the units are greater than or equal to 300, assign "High Usage". Otherwise, check again. 
If the units are greater than or equal to 200, assign "Moderate Usage"; otherwise, assign "Normal Usage".
 If the units are less than 100, assign "Low Usage". Display the usage category.

Input:
Units = 220

Output:
Usage Category = Moderate Usage
"""
Units=int(input("Enter the Units consumed  : "))

if Units>=100:
    if Units>=300:
        print("High Usage")
    elif Units>=200:
        print("Moderate Usage")
    else:
        print("Normal Usage ")
else:
    print("Low Usage ")
