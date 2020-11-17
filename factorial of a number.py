n = int(input("Enter a number to find it's factorial:"))
temp = n
fac = 1
while temp>0:
    fac = fac * temp
    temp = temp - 1
print("The factorial of",n,"is",fac)