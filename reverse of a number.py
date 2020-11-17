def rev(n):
    temp=n
    r = 0
    while(temp!=0):
        temp = temp%10
        r = r * 10 + temp
        temp = temp//10
        return r


x = int(input("Enter a number to find it's factorial:"))
y =rev(x)
print("The reverse of",x," is:",y)
