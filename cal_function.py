def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def pro(a,b):
    return a*b

def fact(a):
    fact = 1
    for i in range(1,a+1):
        fact=fact*i
    return fact

def even(a,b):
    even=0
    for i in range(a,b+1):
        if i%2==0:
            even+=i
    return even

def fib(n):
    a=0
    b=1
    for i in range(0,n):
        print(a,end=" ")
        a,b=b,a+b