"""
Assignment 9: Petrol Cost Calculation

You traveled a certain distance. Based on mileage and petrol price, calculate fuel used and total cost.

Input:
Distance = 450 km
Mileage = 15 km/litre
Petrol price = 110/litre

Expected Output:
Petrol Used = 30.0 litres
Total Cost = 3300.0
"""
dist=int(input("Enter the distance"))
Mileage=int(input("Enter mileage (km/litre)"))
petrolprice=int(input("Enter the value of petrol "))
amt=(dist/Mileage)*petrolprice
petrolused=dist/Mileage

print("petrol used : ",petrolused)
print("Total cost fuel : ",amt)

