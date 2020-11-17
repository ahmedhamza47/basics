class rectangle:
    def __init__(self):
        self.l = int(input("Enter value:"))
        self.b = int(input("Enter breadth:"))

    def area(self):
        area = self.l * self.b
        print(area)

r1 = rectangle()
r1.area()
