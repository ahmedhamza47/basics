print("The prime numbers from 1 to 100 are :")
for num in range(1,100):
    count = 0
    for i in range(2,(num//2)):
        if num%i ==0:
            count= count+1
            break
    if(count==0)and(num!=-1):
        print(num,end=" ")
