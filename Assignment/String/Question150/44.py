"""
44Check if two strings are anagrams. S1 = "listen", S2 = "silent" TRUE

"""
s1=input("Enter a string: ")
s2=input("Enter another string: ")
if len(s1)==len(s2):
    if sorted(s1)==sorted(s2):
        print("True")
    else:
        print("False")
else:
    print("False")