"""Assignment 8: Data Storage Converter

Write a Python program that:

Accepts value in MB.
Converts into GB.

Input:
MB = 2048

Output:
GB = 2.0
"""
mb=int(input("Enter the vaue in MB : "))
gb=mb/1024
print("Converts into GB : ",gb)