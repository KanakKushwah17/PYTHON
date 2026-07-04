"""
42Check if two strings are equal without equals(). S1 = "abc", S2 = "abc" TRUE

"""
s1=input("Enter first string: ")
s2=input("Enter second string: ")
count=0
if len(s1)==len(s2):
    for i in range(0,len(s1)):
        if s1[i]!=s2[i]:
            count=1
            break
    if count==0:
        print("True")
    else:
        print("False")
else:
    print("False")

