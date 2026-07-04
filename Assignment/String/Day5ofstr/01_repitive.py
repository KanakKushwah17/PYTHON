"""
1.
Find the Longest Substring Without Repeating Characters
Cybersecurity Session Tracking System

A cybersecurity company monitors user session IDs generated during secure login sessions.

To detect suspicious repeated patterns, the company wants a Python program that finds the longest substring containing no repeated characters.

Input:
abcabcbb
Output:
abc
"""
s=input("Enter string ")

for i in range(len(s)):
    visit = []
    for j in range(i,len(s)):
        if s[j] not in visit:
            visit.append(s[j])
        else:
            break
print("".join(visit))
