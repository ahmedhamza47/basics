from array import *
try:
    mark = array('f',[])
    n = int(input("Enter the no. of subjects:"))
    for i in range(n):
        x = float(input("Enter marks in subject :"))
        mark.append(x)

    print("The marks in subjects are:")
    for i in range(n):
        print(mark[i])
    result = 0
    for i in range(n):
        result+= mark[i]

    percent = (result/(n*100))*100
    print("The total marks obtained is:",result)
    print("The percentage obtained is:",percent)
    if(result<=(n*50)):
        print("The student is fail")
    else:
        print("The student is pass")

except ValueError as e:
    print("Invalid Input")
