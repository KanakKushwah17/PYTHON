"""
53Remove punctuation. S = "Hello, world!" "Hello world"

"""
s=input("Enter a string: ")

punct=",.!?;:'\"-()"

store=""

for i in s:

    if i not in punct:
        store=store+i

print(store)