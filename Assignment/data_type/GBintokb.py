"""
Assignment 6: Data Storage Conversion

A user wants to convert data from GB into MB and KB.

Input:
Data = 5 GB

Expected Output:
In MB = 5120.0
In KB = 5242880.0
"""
GB=int(input("Enter the Data in GB :"))
MB=GB*1024
print("In MB : ",MB)
KB=GB*1048576
print("In KB : ",KB )