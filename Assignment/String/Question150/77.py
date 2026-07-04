"""
77Find the longest substring that appears at both ends. S = "abracadabra" "abra"

"""
s=input("Enter strings: ")


rev=" "

ls=s[: :-1]
for i in s:
    found = 1
    for j in ls:
        if i!=j:
            found=0
            break
        else:
            continue
    if found==1:
        rev=rev+i
print(rev)




