for i in range(5):
    user_input = int(input("Guess the number: "))
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
elif (user_input > com_input - 7):
    print("The number is too low")
elif (user_input == com_input):
    print("You have guessed the right number.")
    print("!!!!Congratulations!!!!")
    break