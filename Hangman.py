import random as rd

names = ['HAMZA']
print("Welcome to HANGMAN")

computer = rd.choice(names)
if(computer== 'HAMZA'):
    nm = 'H__Z_'
    print(nm)

    for i in (nm):
        x = input("Guess the  missing Alphabet:").upper()
        if(x=='A'):
            nm[1] = 'A'
            nm[4] = 'A'
            print(nm)
        if(x=='M'):
            temp = 'M'
            nm[3] = temp
            print(nm)
        elif(nm==computer):
            print("You guess correct")
            break









