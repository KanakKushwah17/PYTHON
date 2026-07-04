"""a=[1,2,[3,4,[5,6]]]
print(a)
print(len(a))
print(len(a[2]))
print(len(a[2][2]))
"""

"""A = [
[
[1,2],
[3,4]
],
[
[7,8],
[9,10]
]
]

print(A)                     # OUTPUT - [[[1, 2], [3, 4]], [[7, 8], [9, 10]]]
print(len(A))                # OUTPUT - 2
print(len(A[0]))             # OUTPUT - 2
print(len(A[2][2]))          # OUTPUT - 2

"""

"""A = [
[
[1,2],
[3,4]
],
[
[7,8],
[9,10]
]
]

print(A)
for i in range(len(A)):
    print("Layer ",i)
    for j in range(len(A[i])):
        for k in range(len(A[i][j])):
            print(A[i][j][k],end=" ")
        print()
    print()"""

"""list1=[1,1,1,1]
count=0
k=2
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]+list1[j]==k:
            count=count+1
print(count)"""


