from pickle import TRUE
import random

def take_initial_no_pencils():
    no_of_pencils = input("How many pencils would you like to use:")
    while True:
        if no_of_pencils.strip().isdigit():
            if int(no_of_pencils) < 10:
                no_of_pencils = input("The number of pencils should be greater than equal to 10: ")
                continue
            else: 
                break
        else:
            no_of_pencils = input("The number of pencils should be numeric")
    return int(no_of_pencils)

def player_name():
    player = input("Who will be the first (You, computer):")   
    while True:
        if player == "You" or player == "computer":
            break
        else:
            player = input("Choose between 'You' and 'computer'")
    return player

def bot_turn(no_of_pencils):
    if no_of_pencils == 1:
        bot_input = 1
    elif (no_of_pencils - 1) % 4 == 0:
        bot_input = random.randint(1, 3)
    elif (no_of_pencils)%4 == 0:
        bot_input = 3
    elif (no_of_pencils)%4 == 3:
        bot_input = 2
    elif (no_of_pencils)%4 == 2:
        bot_input = 1
    print(bot_input)
    return no_of_pencils - bot_input

def player_turn(no_of_pencils):
    player_input = input()
    while TRUE:
        if player_input.strip().isdigit():
            if player_input == "1" or player_input == "2" or player_input == "3":
                if int(no_of_pencils) - int(player_input) == 0:
                    break
                elif int(no_of_pencils) - int(player_input) < 0:
                    player_input = input("Too many pencils were taken")
                    continue
                break
            else:
                player_input = input("Possible values: '1', '2' or '3'")
        else:
            player_input = input("Possible values: '1', '2' or '3'")
    return (no_of_pencils - int(player_input))


no_of_pencils = take_initial_no_pencils()


player = player_name()
while no_of_pencils != 0:
    print("")
    print("|" * int(no_of_pencils))
    print(f"Now number of pencils = {no_of_pencils}")
    
    if player == "You":
        print("You's turn!")
        no_of_pencils = player_turn(no_of_pencils)
        player = "computer"
        continue
    elif player == "computer":
        print("computer's turn!")
        no_of_pencils = bot_turn(no_of_pencils)
        player = "You"
        continue
print(f"{player} won")