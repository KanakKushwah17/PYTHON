"""
47Check for substring using concatenation trick. S1="CDAB", S2="ABCD" True (S1 is in S2+S2)

"""
s1=input("Enter a string: ")
s2=input("Enter another string: ")
if len(s1)==len(s2):
    if sorted(s1)==sorted(s2):
        print("True")
    else:
        print("False")