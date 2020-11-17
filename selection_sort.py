arr = [2,4,6,1,3]

for i in range(4):
    minpos = i
    for j in range(i,5):
        if arr[j]<arr[minpos]:
            minpos = j

    temp = arr[i]
    arr[i] = arr[minpos]
    arr[minpos]= temp

print("The sorted array is:",arr)
