s1=input("Enter first string ")
s2=input("Enter second string ")
if len(s1)!=len(s2):
    print("strings are not anagrams")
else:
    visited=[]
    flag=1
    i=0
    while i<len(s1):
        ch=s1[i]
        if ch not in visited:
            c1=0
            c2=0
            j=0
            while j<len(s1):
                if s1[j]==ch:
                    c1=c1+1
                j=j+1
            j=0
            while j<len(s2):
                if s2[j]==ch:
                    c2=c2+1
                j=j+1
            if c1!=c2:
                flag=0
                break
            visited.append(ch)
        i=i+1
    if flag==1:
        print("string are anagrams ")
    else:
        print("strings are not anagram")