"""
73Find the longest palindromic substring. S = "babad" "bab" (or "aba")

"""
s=input("Enter a string: ")
max=""
for i in range(len(s)):
    for j in range(len(s)):
        sub=s[i:j+1]
        if sub[::-1]==sub:
            if len(sub)>len(max):
                max=sub
print("The longest palindromic substring is",max)
