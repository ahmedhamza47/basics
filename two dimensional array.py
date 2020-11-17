from numpy import *
A = array([[],[]])
B = array([[],[]])
C = array([[],[]])

print("Enter the elements of matrix A:")
for i in range(3):
    for j in range(3):
        x = int(input())
        A[i][j] = x

print("Enter the elements of matrix B:")
for i in range(3):
    for j in range(2):
        y = int(input())
        B[i][j] = y


for i in range(3):
    for j in range(2):
        C[i][j] = A[i][j] + B[i][j]

print("The sum of matrix is:")
for i in range(2):
    for j in range(2):
        print(C[i][j])




