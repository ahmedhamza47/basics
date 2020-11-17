num = int(input("Enter a number to find if its armstrong:"))
temp = num
arm = 0
for i in range(3):
    rem = temp %10
    arm = arm + rem ** 3
    temp = temp //10

if(num==arm):
    print(num,"is armstrong number")
else:
    print(num,"is not an armstrong number")

