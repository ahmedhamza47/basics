def fac(n):
    if (n==0)or (n==1):
        return 1
    else:
        return n*fac(n-1)

print("Enter a number to find its factorial:")
x = int(input())
y = fac(x)
print("The factorial of",x,"is",y)
