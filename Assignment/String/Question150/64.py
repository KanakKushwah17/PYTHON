"""
64Count frequency of each vowel. S = "programming" o: 1, a: 1 (e, i, u: 0)

"""
s=input("Enter string: ")

vowels="aeiou"

for i in vowels:

    count=0

    for j in s:

        if i==j:
            count=count+1

    print(i,":",count)