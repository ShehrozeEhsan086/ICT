print("ROCK PAPER SCISSORS GAME")

import random

win_count_user = 0
win_count_comp = 0


while win_count_comp <= 2 and win_count_user <= 2:
    
    user_choice = int(input("\nEnter 0 for Scissor, 1 for Rock and 2 for Paper: "))
    computer = random.randint(0,2)

    if user_choice == 0:
        if computer == 0:
            print("\n Its a DRAW. The user and computer both chose Scissors. \n")
        elif computer == 1:
            print("\n Computer WINS. Computer chose Rock while user chose Scissors. \n")
            win_count_comp += 1
        else:
            print("\n User WINS. Computer chose Paper while user chose Scissors. \n")
            win_count_user += 1
    
    elif user_choice == 1:
        if computer == 0:
            print("\n User WINS. Computer chose Scissors and user chose Rock. \n")
            win_count_user += 1
        elif computer == 1:
            print("\n Its a DRAW. The user and computer boths chose Rock. \n")
        else:
            print("\n Computer WINS. Computer chose Paper and user chose Rock. \n")
            win_count_comp += 1
    
    elif user_choice == 2:
        if computer == 0:
            print("\n Computer WINS. Computer chose Scissors and user chose Paper. \n")
            win_count_comp += 1
        elif computer == 1:
            print("\n User WINS. Computer chose Rock and user chose Paper. \n")
            win_count_user
        else:
            print("\n Its a DRAW. The user and computer both chose Paper. \n")
    
    else:
        print("\n Invalid input, Try again and check for spelling. \n")

    print(f"SCORE: Computer = {win_count_comp}\nUser = {win_count_user}")
    
    if win_count_comp == 3 or win_count_user == 3:
        if win_count_comp == 3:
            print("\nComputer won more than twice.")
        elif win_count_user ==  3:
            print("\nUser won more than twice.")
        else:
            continue
        Replay = input(" \n Wanna play again? (Y/N) : ")
        replay = Replay.lower() # removes case sensitivity 
        if replay == "y":
            win_count_comp, win_count_user = 0,0
        elif replay == "n":
            break 
        else:
            print("Please enter valid values.")
            break

# Shehroze Ehsan 086 