"""
3.
Industrial Sensor Peak Energy Monitoring System

Problem Statement

A factory machine records energy consumption at regular intervals.

A peak is defined as a value greater than or equal to its neighbors.

Tasks:

Find all peak energy values
Compute sum of squares of peak values
Compute average of peak values
Return difference between max peak and min peak
If no peaks, return -1

Test Case 1

Input:
energy = [20, 40, 30, 60, 50]

Output:
Peaks = [40, 60]
Sum of squares = 5200
Average = 50
Difference = 20

Test Case 2

Input:
energy = [10, 20, 15, 25, 20, 30]

Output:
Peaks = [20, 25, 30]
Sum of squares = 1525
Average = 25
Difference = 10

Test Case 3

Input:
energy = [5]

Output:
Peaks = [5]
Sum of squares = 25
Average = 5
Difference = 0
"""
from traceback import format_list

n=int(input("Enter number"))
arr=[]
for i in range(n):
    x=int(input("Enter element "))
    arr.append(x)
print(arr)

sum=0
prod=1
listofpeak=[]
peakindex=-1
for i in range(n):
    if i==0:
        if n==1 or arr[i]>=arr[i+1]:
            peakindex=i
            listofpeak.append(arr[i])
    elif i==n-1:
        if arr[i]>=arr[i-1]:
            peakindex=i
            listofpeak.append(arr[i])
    else:
        if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]:
            peakindex=i
            listofpeak.append(arr[i])

print("Peak element is ",listofpeak)

for i in listofpeak:
    sqr=i*i
    sum=sum+sqr
print("sum square :", sum)

count=0

sum=0
for i in listofpeak:
    sum=sum+i
    count = count + 1
    
avg=sum//count
print("Average :",avg)

max=0
for i in listofpeak:
    if max<i:
        max=i


min=999
for i in listofpeak:
    if min>i:
        min=i

diff=abs(min-max)
print("Difference :",diff)