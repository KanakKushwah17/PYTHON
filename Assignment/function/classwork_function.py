"""def sum():
    a=10
    b=20
    c=a+b
    print("sum =",c)
sum()
"""

"""def sum(a,b):
    c=a+b
    print("sum =",c)
a=int(input("enter first number"))
b=int(input("enter second number"))
sum(a,b)"""

"""def sum(a,b):
    c=a+b
    return c
def main():
    x=sum(10,20)
    c=sum(11,22)
    print(sum(66,77))
    print(c)
    
"""
"""def add(a,b):
    c=a+b
    return c
def sub(a,b):
    d=a-b
    return d
def mult(a,b):
    e=a*b
    return e


def main():
    while True:
        print("Menu")
        print("1. sum")
        print("2. subtract ")
        print("3. multiply")
        choice = int(input("Enter your choice:"))
        a = int(input("enter first number"))
        b = int(input("enter second number"))
        match choice:
            case 1:
                print("sum =",add(a,b))
            case 2:
                print("subtraction =",sub(a,b))
            case 3:
                print("Multiply =",mult(a,b))

main()
"""
"""def hello(name,*marks):
    print("Name :",name)
    print("Marks :",marks)
    print("Marks",*marks)
hello("deepika",10,20,30,)
"""
"""l1=[10,20,30,40]
def add(*l2):
    return sum(l2)
print(add(*l1))"""

"""def add(a,b,c,/):
    print(a+b+c)
add(10,20,30)
#add(a=100,b=200,c=300)
    
"""
"""
def display(a,*,b,c):
    print(a+b+c)
display(a=10,b=20,c=30)"""

"""fun=lambda n:n*n
print(fun(5))
"""
"""l1=[10,20,30,40,50,60,70]
def add(*l2):
    return sum(l2)
print(add(*l1))
"""


"""max=lambda a,b:print(a) if a>b else print(b)
max(10,20)
"""

"""def sq(x):
    return x*x
l1=[10,20,30]
print(list(map(sq,l1)))
"""

"""
l=["yogita","hello","kanak"]
r=map(lambda a:a.capitalize(),l)
print(list(r))"""


"""l=["yogita","hello","kanak"]
r=map(lambda a:a.upper(),l)
print(list(r))
"""
"""l=["yogita","hello","kanak"]
r=map(lambda a:len(a),l)
print(list(r))"""

"""l1=[10,20,30]
l2=[40,50,60]
r=map(lambda a,b:a+b,l1,l2)
print(list(r))"""

"""l1=[1,20,3,40,5,60,7,80]
r=map(lambda a:"even" if a%2==0 else "odd",l1)
print(list(r))

"""

"""l1=[92,60,31,56]
r=map(lambda a:"A" if a>90 else "B" if a>60 else "C" if a>40 else "Fail" ,l1)
print(list(r))"""


"""l1 =[92,60,31,56,77,43]
r=filter(lambda a:a%2==0,l1)
print(list(r))"""

"""l1=["kanak", "anamika ", "aman ", "rajni ", "madhur"]
r=filter(lambda x:x.startswith('a'),l1)
print(list(r))"""

"""l1=["kanak", "anamika ", "aman ", "rajni ", "madhur"]
r=filter(lambda x:len(x)>5  ,l1)
print(list(r))"""

"""l1=("Hello","","Kanak","4","5","","","Why"," hehehe")
r=filter(lambda x:len(x)>0,l1)
print(list(r))"""

"""l1=[1,2,3,4,5,6,7,8,9]
r=filter(lambda x:x%2==0,(map(lambda a:a*a,l1)))
print(list(r))"""

"""l1=["kanak","hello","madam","what "]
r=map(lambda x:x[::-1],l1)
print(list(r))"""

"""
num=[5,2,8,6,7,]
a=sorted(num)
print(a)
b=sorted(num,reverse=True)
print(b)

x=sorted(num,key=lambda x:x)
print(x)"""



"""def sum(n):
    if n==0:
        return 0
    return n+sum(n-1)

def main():
    n=int(input("Enter a number:"))
    x=sum(n)
    print(x)
main()"""

"""def pow(a,b):
    if b==0:
        return 1
    return a*pow(a,b-1)
def main():
    n=int(input("Enter a number:"))
    y=int(input("Enter another number:"))
    x=pow(n,y)
    print(x)
main()"""

"""def basec(n):
    if n==0:
        return 0
    return 1+basec(n//10)
def main():
    n=int(input("Enter a number:"))
    x=basec(n)
    print(x)
main()"""

"""def outer():
    def test():
        print("Inside function")
        print(len([10,20,30,40,50,60,70]))
    test()
outer()"""

"""l=[1,2,3,4,5,6,7]
x=map(lambda x:x+2,l)
y=filter(lambda x:x%2==0,l)
print(list(x))
print(list(y))"""

"""def add(a,b):
   # this function adds two numbers
    return a+b
print(add(3,4))
print(add.__doc__)
print(int.__doc__)
"""



