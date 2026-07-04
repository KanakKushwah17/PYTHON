"""
57Merge two strings alternatively. S1 = "ABC", S2 = "def" "AdBeCf"

"""
s1=input("Enter first string: ")
s2=input("Enter second string: ")
new=""
i=0
while i >len(s1) or i <len(s2):
    new=new+s1[i]+s2[i]
    i=i+1
print(new)

