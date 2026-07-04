"""
90Remove adjacent duplicates recursively. S = "azxxzy" "ay"

"""
s = input("Enter string ")

res = ""

for i in s:

    if len(res) > 0 and res[-1] == i:
        res = res[:-1]
    else:
        res = res + i

print(res)