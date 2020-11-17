n1 = int(input("Enter starting number:"))
n2 = int(input("Enter ending number:"))
print("The even numbers are: ")
for i in range(n1,n2):
    if(i%2==0):
        print(i)
print("The odd numbers are: ")
for i in range(n1,n2):
    if(i%2 != 0):
        print(i)