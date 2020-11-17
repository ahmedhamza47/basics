class rectangle:
    def __init__(self,l,b):
        self.l = l
        self.b = b

    def calculate(self):
        area = self.l * self.b
        print("The area of rectangle is:",area)

print("Enter length and breadth:")
x = int(input())
y = int(input())

r1 = rectangle(x,y)
r1.calculate()


