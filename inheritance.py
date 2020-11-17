class data:
    def __init__(self):
        self.a = int(input("Enter first number:"))
        self.b = int(input("Enter second number:"))

class sum(data):
    def show(self):
        add = self.a + self.b
        print("The sum of two number is",add)

class sub(data):
    def show(self):
        sub = self.a - self.b
        print("The difference of two number is",sub)


s1 = sum()
s1.show()
s2 = sub()
s2.show()