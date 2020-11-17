arr = [1,4,8,22,56,89,100]
pos = -1

def binary(arr,n):
    l = 0
    u = len(arr)-1
    for l in range(u):
        mid = (l+u)/2
        if(arr[mid] == n):
            globals()['pos'] = mid
            return True

        else:
            if(n>arr[mid]):
                l = mid
            else:
                u = mid

x = int(input("Enter the number that you want to find:"))
if binary(arr,x):
    print("number found at",pos+1,"th position")
else:
    print("number not found.")



