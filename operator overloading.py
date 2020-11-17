#complex numbers

class complex:
    def __init__(self,c1,c2):
        self.c1 = c1
        self.c2 = c2

    def __add__(self, other):
        c1 = self.c1 + other.c1
        c2 = self.c2 + other.c2
        x3 = complex(c1,c2)
        return x3
x1 = complex(2,3)
x2 = complex(3,4)

x3 = x1 + x2
print(x3.c1,"+",x3.c2,"i")

