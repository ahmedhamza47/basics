
j = 0
print("THE ARMSTRONG NUMBERS ARE..")
for i in range(1,1000):
    arm = 0
    temp = i
    while temp > 0:
        rem = temp % 10
        arm = arm + rem ** 3
        temp = temp // 10
    if(i == arm):
        print(i)


