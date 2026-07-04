"""
32Count frequency of each word. S = "apple banana apple" apple: 2, banana: 1
"""

s = "apple banana banana apple banana"

words = []
temp = ""
visit=[]
for ch in s:
    if ch != " ":
        temp += ch
    else:
        words.append(temp)
        temp = ""

words.append(temp)

print(words)
for item in words:
    count = 0

    for x in words:
        if x == item:
            count += 1

    if item not in visit:
        print(item, ":", count)
        visit.append(item)

