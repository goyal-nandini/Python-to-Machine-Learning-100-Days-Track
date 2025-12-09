import random
import art

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
num = random.randint(1, 100)
level = input("Choose a difficulty, Type 'easy' or 'hard': ").lower()

def decision_maker(guess):
    # guessed = False
    # for _ in range(attempts): 👎
        if guess == num:
            print(f"Correct! Superb You have guessed in {attempts} attempts!")
            # guessed = True
            return True 
        elif guess > num:
            print(f"Too high.\nGuess again.")
            # attempts -= 1
            # print(f"You have {attempts} attempts remaining to guess the number.") 👎
        elif guess < num:
            print(f"Too low.\nGuess again.")
            # attempts -= 1
            # print(f"You have {attempts} attempts remaining to guess the number.") 👎
        
# 🚨📝 FIX:
if level == "easy":
    attempts = 10
elif level == "hard":
    attempts = 5
else:
    print("Invalid Entry. Game Over!")
    exit()

print(f"You have {attempts} attempts remaining to guess the number.")

while attempts > 0:
        guess = int(input("Make a guess: "))
        guessed = decision_maker(guess)
        attempts -= 1
        if guessed == True:
            break
        if attempts > 0:
            print(f"You have {attempts} attempts remaining.")
        else:
            print("You lose! Your attempts are over. Better luck next time.")

# 👎 TOO REPETITIVE CODE!!🚨📝
# if level == "easy":
#     print("You have 10 attempts remainig to guess the number.")
#     attempts = 10
#     while attempts > 0:
#         guess = int(input("Make a guess: "))
#         guessed = decision_maker(guess, guessed=False) 
#         attempts -= 1
#         # print(f"You have {attempts} attempts remaining to guess the number.") 👎
#         if attempts > 0:
#             print(f"You have {attempts} attempts remaining.")
#         else:
#             print("You lose! Your attempts are over. Better luck next time.")
#     #     if guessed == True: 👎
#     #         break
#     # if guessed == False:
#     #     print("You lose as Your attempts got over. Better luck next time!\nRefresh the page to start again.")
# elif level == "hard":
#     print("You have 5 attempts remaining to guess the number.")
#     attempts = 5
#     while attempts > 0: # 👎 TOO REPETITIVE CODE!!🚨📝
#         guess = int(input("Make a guess: "))
#         guessed = decision_maker(guess, guessed=False)
#         attempts -= 1
#         # print(f"You have {attempts} attempts remaining to guess the number.") 👎
#         if attempts > 0:
#             print(f"You have {attempts} attempts remaining.")
#         else:
#             print("You lose! Your attempts are over. Better luck next time.")
#     #     if guessed == True: 👎
#     #         break
#     # if guessed == False:
#     #     print("You lose as Your attempts got over. Better luck next time!\nRefresh the page to start again.")
# else:
#     print("Invalid Entry. Game Over!")
