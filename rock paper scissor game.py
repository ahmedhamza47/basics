import random as rd
import time

print("Welcome to the Rock Paper and Scissors:")
print("This game is a base of 5")
winu,winc,draw= 0,0,0
i = 1
computer = ['Rock', 'Scissor', 'Paper']
for i in range(5):
    print("Game",i+1)

    user_input = input("Enter your choice:").upper()
    if user_input == "R":
        print("You have selected rock")
    elif user_input == "P":
        print("You have selected Paper")
    elif user_input == "S":
        print("You have selected Scissors")
    else:
        print("Invalid entry")

    com_input = rd.choice(computer)
    print("Computer selected:",com_input)
    time.sleep(1)

    if  user_input == "R" and com_input == "Scissor" :
        print("You Won")
        winu = winu + 1

    elif user_input == "R" and com_input == "Paper" :
        print("You lose")
        winc = winc + 1

    if  user_input == "S" and com_input == "Paper" :
        print("You Won")
        winu = winu + 1
    elif user_input == "S" and com_input == "Rock" :
        print("You lose")
        winc = winc + 1

    if  user_input == "P" and com_input == "Scissor" :
        print("You Lose")
        winc = winc + 1
    elif user_input == "P" and com_input == "Rock" :
        print("You Won")
        winu = winu + 1

    elif (user_input == "S" and com_input == "Scissor") or (user_input == "P" and com_input == "Paper")or(user_input == "R" and com_input == "Rock"):
        print("Game tied")
        draw = draw+1
print("\n")
print("User won ",winu,"times")
print("Computer won ",winc,"times")
if(winu>winc):
     print("Hence user won")
elif(winc>winu):
    print("Hence computer won")
else:
    print("Game Draw")








