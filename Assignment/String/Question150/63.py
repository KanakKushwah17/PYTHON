"""
63Count frequency of each character. S = "aabcc" a: 2, b: 1, c: 2

"""
s=input("Enter string: ")

visit=""

for i in s:

    if i not in visit:

        count=0

        for j in s:

            if i==j:
                count=count+1

        print(i,":",count)

        visit=visit+i
