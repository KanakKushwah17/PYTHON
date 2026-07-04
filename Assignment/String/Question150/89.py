"""
89Remove 'b' and 'ac' from a string. S = "abacbb" "c"
"""

s = input("Enter a string: ")

new = ""
i = 0

while i < len(s):

    # Remove 'b'
    if s[i] == 'b':
        i += 1

    # Remove "ac"
    elif i + 1 < len(s) and s[i] == 'a' and s[i + 1] == 'c':
        i += 2

    # Keep remaining characters
    else:
        new += s[i]
        i += 1

print("Output:", new)

