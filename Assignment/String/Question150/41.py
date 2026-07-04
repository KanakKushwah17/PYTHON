"""
41Check if a string contains a substring (without using built-in method). S1 = "Hello", Sub="ell" TRUE

"""
str=input("Enter a string: ")
substr=input("Enter a substring: ")
k=0
for i in range(len(str)):
    for j in range(i,len(str)):
        sub=str[i:j+1]
        if sub == substr:
            k=1
if k==0:
    print("FALSE")
else:
    print("TRUE")

