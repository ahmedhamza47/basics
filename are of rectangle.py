class rectangle:
    l = int(input("Enter lenght:"))
    b = int(input("Enter breadth:"))

    def area(cls):
        sum = cls.l * cls.b
        print(sum)

r1 = rectangle()
r1.area()
