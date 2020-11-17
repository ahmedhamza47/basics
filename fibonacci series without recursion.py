def fib(n):
    a=0
    b=1
    c=1
    for i in range(n):
        print(a)
        a=b
        b=c
        c=a+b

x=int(input("Enter the limit of fibonacci series:"))
fib(x)
