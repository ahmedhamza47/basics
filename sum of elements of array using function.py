from numpy import *
def arr(A,p):
    add =0
    A = zeros()
    for i in range(p):
        add = add + A[i]
    return add



B = zeros(n,int)
print("Enter the limit of array:")
n = int(input())
print("Enter the elements of array:")
for i in range(n):
    x = int(input())
    B[i] = x

sum = arr(B,n)
print("The sum of array is:",sum)




