arr = [1,2,3,4,8,9]
print("Enter the number that you want to search:")
x = int(input())
count =1
for i in arr:
    if (i == x):
        print("The number is found at", count, "th place")
        break
    count= count+1
else:
    print("Number not found")
