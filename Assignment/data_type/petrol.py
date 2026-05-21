"""Assignment 9: Fuel Cost Calculator

Write a Python program that:

Accepts distance (km), mileage (km/litre), and petrol price.
Calculates total fuel cost.

Input:
Distance = 100
Mileage = 20
Petrol Price = 100

Output:
Cost = 500
"""
dist=int(input("Enter the distance"))
Mileage=int(input("Enter mileage (km/litre)"))
petrolprice=int(input("Enter the value of petrol "))
amt=(dist/Mileage)*petrolprice
print("Total cost fuel : ",amt)