class A:
    def show(self):
        print("In A")

class B(A):
    def show(self):
        print("In B")

a1 = B()
a1.show()
#it wont print show of A