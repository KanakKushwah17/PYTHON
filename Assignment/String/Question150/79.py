"""
79Divide a string into n equal parts. S = "abcdef", n = 3 "ab", "cd", "ef"

"""
s=input("Enter the String: ")
n=int(input("Enter the Number: "))
if len(s)%n!=0:
    print("Cannot divide into equal parts")
else:
    size=len(s)//n
    for i in range(0,len(s),size):
        print(s[i:i+size])


