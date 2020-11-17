

def person(name,**data):
    print(name)
    for i,j  in data.items():
        print(i,j)

person('hamza',age = 18,city = 'mumbai')

