"""
66Count number of sentences in a paragraph. P = "This. Is. Test." 3

"""
p=input("Enter paragraph: ")

count=0

for i in p:
    if i=='.':
        count=count+1

print(count)