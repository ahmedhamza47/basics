
def name(list):
    print("The names with more than 5 letters are:")
    for i in list:
        if len(i)>10:
            print(i)
    else:
        print("-----")

    print("The names with less than 5 letters are:")
    for i in list:
        if len(i)<=5:
            print(i)
    else:
        print("-----")


list = []
print("Enter 10 names:")
for i in range(10):
    x = input()
    list.append(x)

name(list)