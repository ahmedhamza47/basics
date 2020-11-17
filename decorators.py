def div(a,b):
    print(a/b)

def new_div(func):
    def inner(c,d):
        if c<d:
            c,d = d,c
            return func(c,d)
    return inner


divide = new_div(div)
divide(2,4)

