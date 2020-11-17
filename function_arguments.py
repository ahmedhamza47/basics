def add_mul(*b):
    c = 0
    for i in b:
        c = c + i
    e= 1
    for i in b:
        e = e*i

    return c,e

r1,r2 = add_mul(1,2,3,4,5)
print(r1)
print(r2)


