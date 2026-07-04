"""
36Reverse order of words. S = "one two three" "three two one"

"""
s = "one two three"

word = ""
rev = ""

for ch in s:
    if ch != " ":
        word += ch
    else:
        rev = word + " " + rev
        word = ""

rev = word + " " + rev

print(rev)