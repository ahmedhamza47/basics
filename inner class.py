class geometry:
    def __init__(self):
        self.rectangle = self.rectangle()
        self.triangle = self.triangle()

    class rectangle:
        def __init__(self):
            self.l = int(input("Enter length:"))
            self.b = int(input("Enter breadth:"))
        def show(self):
            area = self.l * self.b
            print("The area of rectangle is:",area)

    class triangle:
        def __init__(self):
            self.h = int(input("Enter height:"))
            self.b = int(input("Enter base:"))

        def show(self):
            area = 0.5 * self.b * self.h
            print("The area of triangle  is:",area)

r1 = geometry.rectangle()
r1.show()
t1 = geometry.triangle()
t1.show()
