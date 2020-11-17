n = int(input("enter the limit to find the numbers:"))
for i in range(0,n+1):
    if (i%4 ==0) and (i%5 ==0):
        print(i)