"""1. Second Largest Without sort() or max()

Write a program to find the second largest unique element in a list.

Input:

[12, 45, 67, 45, 89, 67]

Output:

67
    """
    
    
"""n=int(input("Enter the number: "))
target=int(input("Enter the target: "))

num=[]
for i in range(n):
    num.append(int(input("Enter the number: ")))

print(num)
max=num[0]
for i in num:
    if i<max:
        i=max
print(max)"""


"""2. Frequency Without count()

Print the frequency of every element without using count().

Input:

[1, 2, 1, 3, 2, 1, 4]

Output:

1 -> 3
2 -> 2
3 -> 1
4 -> 1
    """
    
"""n=int(input("Enter Numbers :   "))
nums=[]
for i in range(n):
    list=int(input("Enter list : "))
    nums.append(list)

nums=sorted(nums)
print(nums)
count=0
for i in range(len(nums)-1):
    if nums[i]== nums[i+1]:
        count=count+1
    else:
        print(nums[i],"=",count)
        count=1
print(nums[-1], "=", count)
   """     
"""freq = {}

for i in nums:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for key in freq:
    print(key, "=", freq[key])"""


"""3. Rotate List

Rotate the list to the right by k positions.

Input:

List: [1,2,3,4,5]
k = 2

Output:

[4,5,1,2,3]
    """
    
"""n=int(input("Enter Numbers :   "))
k=int(input("Enter rotate "))
nums=[]
for i in range(n):
    list=int(input("Enter list : "))
    nums.append(list)

print(nums)
new=[]
for j in range(k+1,len(nums)):
    new.append(nums[j])
    
for i in range(k+1):
    new.append(nums[i])

    
print(new)"""


"""4. Missing Number

A list contains numbers from 1 to n, but one number is missing.

Find the missing number.

Input:

[1,2,3,5,6,7]

Output:

4
    """
"""n=int(input("Enter Numbers :   "))

nums=[]
for i in range(n):
    list=int(input("Enter list : "))
    nums.append(list)

print(nums)

for i in range(1,len(nums)):
    found=0
    
    for j in nums:
        if j==i:
            found=1
            break
        
    if found==0:
        print(i)
        break"""

"""5. Longest Consecutive Sequence

Find the length of the longest consecutive sequence.

Input:

[100,4,200,1,3,2]

Output:

4

Explanation:

1,2,3,4

"""     
"""n=int(input("Enter Numbers :   "))

nums=[]
for i in range(n):
    list=int(input("Enter list : "))
    nums.append(list)

nums=sorted(nums)
print(nums)      
max=1
count=1
    
for i in range(len(nums)-1):
    if nums[i+1] == nums[i]+1:
        count=count+1
    else:
        count=1
    
    if count>max:
        max=count
print(max)
"""


            
"""6. Remove Duplicates While Preserving Order

Do not use set().

Input:

[5,2,5,1,2,3,1]

Output:

[5,2,1,3]
    """
"""n=int(input("Enter Numbers :   "))

nums=[]
for i in range(n):
    list=int(input("Enter list : "))
    nums.append(list)

print(nums)
new=[]
for i in nums:
    if i not in new:
        new.append(i)
print(new)"""


"""7. Leaders in a List

A leader is greater than all elements to its right.

Input:

[16,17,4,3,5,2]

Output:

17 5 2
    """
"""
n=int(input("Enter Numbers :   "))
nums=[]
for i in range(n):
    list=int(input("Enter list : "))
    nums.append(list)

print(nums)
new=[]
for i in range(len(nums)):
    x=True
    for j in range(i,len(nums)):
        if nums[i]<nums[j]:
           x=False
           break
    if x==True:
        new.append(nums[i])
print(new)"""
            
            
"""8. Find Pair With Given Sum

Print every unique pair whose sum equals the target.

Input:

List = [2,7,11,15,3,6,5]
Target = 9

Output:

(2,7)
(3,6)
    """

"""n=int(input("Enter the number: "))
target=int(input("Enter the target: "))

num=[]
for i in range(n):
    num.append(int(input("Enter the number: ")))

print(num)

for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i]+num[j]==target:
            print(num[i],num[j])"""

"""
10. Maximum Difference

Find the maximum difference arr[j] - arr[i] where j > i.

Input:

[7,1,5,3,6,4]

Output:

5

Explanation:

6 - 1 = 5
    """
n=int(input("Enter the number: "))

num=[]
for i in range(n):
    num.append(int(input("Enter the number: ")))

print(num)
max=0
new=0
for i in range(len(num)):
    for j in range(i,len(num)):
        new=num[j]-num[i]
        if new>0:
            if max<new:
                max=new
            
print(max)
                
            
            
            
            
            
