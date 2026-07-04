"""
5Compare two strings ignoring case. S1 = "Test", S2 = "test" Equal (or 0)

"""
s1=input("Enter the first string: ").lower()
s2=input("Enter the second string: ").lower()
if s1==s2:
    print("The two strings are equal")
else:
    print("The two strings are not equal")
