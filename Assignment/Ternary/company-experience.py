"""
3. Employee Bonus Distribution System
A company provides bonuses based on years of experience.
Experience >10 years → 30% bonus
Experience >5 years → 20% bonus
Otherwise → 10% bonus
Write a program to calculate the total salary after adding bonus using inline if.
"""
exp=int(input("Enter Experience :"))
salary=int(input("Enter salary :"))
Bonus = salary+(salary*30/100) if exp>10  else salary+(salary*20/100) if exp>50 else salary+(salary*10/100)
print("Total salary =",Bonus)
