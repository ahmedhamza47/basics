import random as rd

def game():
    computer = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    com_input = rd.choice(computer)
    print("Guess the number between 1 and 20")
    print("You have only 5 chances")
    try:
        for i in range(5):
            user_input = int(input("Guess number"))
            if (user_input == com_input + 1) or (user_input == com_input + 2) or (user_input == com_input + 3):
                print("The number is a little high.")
            elif (user_input == com_input - 1) or (user_input == com_input - 2) or (user_input == com_input - 3):
                print("The number is a little low.")
            elif (user_input == com_input + 4) or (user_input == com_input + 5) or (user_input == com_input + 6):
                print("The number is  high.")
            elif (user_input == com_input - 4) or (user_input == com_input - 5) or (user_input == com_input - 6):
                print("The number is  low.")
            elif (user_input >= com_input + 7):
                print("The number is too high")
            elif (user_input <= com_input - 7):
                print("The number is too low")
            elif (user_input == com_input):
                print("You have guessed the right number.")
                print("!!!!Congratulations!!!!")
                break
            if (i < 4):
                print("try again")
                print()
        else:
            print()
            print("You couldn't guess the number")
            print("The number was",com_input)
            print()
    except:
        print("Invalid input")
game()

x = input("Would you like to play again \ntype yes or no:")

if(x==1):
    game()
else:
    exit()


