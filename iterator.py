class rectangle:
    def get_input(self):
        self.l = int(input("Enter lenght:"))
        self.b = int(input("Enter breadth:"))

    def mul(self):
        self.area = self.l * self.b
        print(self.area)

r1 = rectangle()
r1.get_input()
r1.mul()


