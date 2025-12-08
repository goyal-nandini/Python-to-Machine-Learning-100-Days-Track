import random
from art import rock, paper, scissors

game_images = [rock, paper, scissors]

print("What do you choose?")
user_choice = int(input("Type 0 for Rock, 1 for paper and 2 for scissors.\n"))

print("You've chosen:")
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

print("Computer chose:")
computer_choice = random.randint(0, 2)
print(game_images[computer_choice])

# from here the logic starts:

if user_choice > 2 or user_choice < 0:  # at the begg o/w user_choice > computer_choice 
    # will pick it...and u win appears ⚠️
    print("You typed an invalid input, You lose!")
    exit()   # ⛔ Game stops here
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice == 2 and user_choice == 0:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose!")
elif computer_choice < user_choice:
    print("You win!")
elif user_choice == computer_choice:
    print("You draw!")


    
    
