"""Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Example 3:
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]
"""

nums=eval(input("enter the list: "))
k=int(input("Enter value k  :  "))



store={}

for i in nums:
    if i in store:
        store[i]+=1   
    else:
        store[i]=1
    
print(store)

sorted_d = dict(sorted(store.items(), key=lambda item: item[1]))

last_k = list(sorted_d.items())[-k:]
res=[]
for key, value in last_k:
    res.append(key)

print(res)




        
    
    

