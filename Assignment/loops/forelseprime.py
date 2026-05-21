
n=int(input("Enter the digit :"))

if n<=1:
   print("Not Prime ")
else:
   for i in range(2,n):
       if n%i==0:
           print("Not prime number ")
           break
   else:
      print("Number is prime ")

