
n = int(input("Enter a number:"))
count = 0
temp  = n
sum,x= 0,0


while(n>0):
    count+=1
    n= n//10

print("The total no. of digits is:",count)

for i in range(count):
    x = temp%10
    temp = temp // 10
    sum = sum + x

print("The sum of the given digit is:",sum)


