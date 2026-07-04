"""
59Rotate characters right by 3 positions. S = "abcde" "cdeab"

"""
s=input("enter string")
l=int(input("enter length"))
store=""

for i in range(l,len(s)):
    store=store+s[i]
for j in range(0,l):
    store=store+s[j]
print(store)
