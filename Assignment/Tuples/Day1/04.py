"""
4.
Find common elements in three sorted arrays.
Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
Note: can you take care of the duplicates without using any additional Data Structure?
Example 1:
Input:
n1 = 6; A = {1, 5, 10, 20, 40, 80}
n2 = 5; B = {6, 7, 20, 80, 100}
n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
Output: 20 80
Explanation: 20 and 80 are the only
common elements in A, B and C.

"""
n1=int(input("Enter a number: "))
n2=int(input("Enter a number: "))
n3=int(input("Enter a number: "))
print("List1")
list1=[]
for i in range(n1):
    list1.append(int(input("Enter list1 number: ")))

print("List2")
list2=[]
for i in range(n2):
    list2.append(int(input("Enter list2 number: ")))

print("List3")
list3=[]
for i in range(n3):
    list3.append(int(input("Enter list3 number: ")))

print("List1",list1)
print("List2",list2)
print("List3",list3)

for i in list1:
    if i in list2:
        if i in list3:
            print(i)




