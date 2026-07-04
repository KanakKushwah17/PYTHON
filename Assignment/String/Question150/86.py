"""
86Print all permutations of a string without repetition. S = "ab"
 o/p  :"ab", "ba"
"""

s=input("Enter a string: ")

for i in range(len(s)):
    for j in range(len(s)):
        if i!=j:
            print(s[i]+s[j])


