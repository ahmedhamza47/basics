nump = int(input("Enter a number:"))
rev = 0
num = nump
leng = len(str(nump))

while(num!=0):
    rem = num % 10
    rev = (rev * 10) + rem
    num = num // 10

print("The number is ",rev)
