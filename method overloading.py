#python directly doesn't support method overloading

class add:
    def sum(self,a=None,b= None,c = None):
        s = 0
        if(a != None and b != None and c!=None):
            s = a+b+c
        elif (a != None and b != None ):
            s = a+b
        else:
            s = a
        return s

a1 = add()

print(a1.sum(2,3))
