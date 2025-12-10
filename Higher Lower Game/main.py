import random
from game_data import data
import art
import os

print(art.logo)

def get_ind():
    '''get random index of data list'''
    return random.randint(0, len(data)-1)

def display_candidate(label, index):
    '''get the unique candidate display on screen'''
    print(f"{label}: {data[index]['name']}, {data[index]['description']} from {data[index]['country']}")
    print(index)

# print(type(get_ind())) -> <class 'int'>

def check(user_input, indA, indB):
    '''check users answer'''
    get_A_followers = data[indA]['follower_count']
    get_B_followers = data[indB]['follower_count']
    # print(f"A: {get_A_followers}")
    # print(f"B: {get_B_followers}")
    get_ans = max(get_A_followers, get_B_followers)

    # print(f"max: {get_ans}")
    if user_input == "A" and get_ans == data[indA]["follower_count"]:
        return True
    elif user_input == "B" and get_ans == data[indB]["follower_count"]:
        return True
    else:
        return False

# game logic:
def game():
    score = 0
    ind1 = get_ind()
    ind2 = get_ind()

    while ind1 == ind2:  # Ensure indices are not the same
        ind2 = get_ind()

    display_candidate("Compare A", ind1)
    print(art.vs)
    display_candidate("Against B", ind2)

    user_input = input("Who has more followers? Type 'A' or 'B': ").upper()

    is_correct = check(user_input, ind1, ind2)
    while is_correct:
        score += 1
        print(f"You're right! Current Score: {score}")
        os.system("cls")
        print(art.logo)
        # again game starts from B candidate!! <- HOW ??!! i think have to prep function for this
        ind1 = ind2
        ind2 = get_ind()

        display_candidate("Compare A", ind1)
        print(art.vs)
        display_candidate("Against B", ind2)

        user_input = input("Who has more followers? Type 'A' or 'B': ").upper()

        while user_input not in ["A", "B"]:
            user_input = input("Invalid input. Please type 'A' or 'B': ").upper()

        is_correct = check(user_input, ind1, ind2)
        
    print(f"Sorry, that's wrong. Final Score: {score}")

game()
    # if check(user_input) == True:
    #     score += 1
    #     print(f"You're right! Current Score: {score}")
    #     # again game starts from B candidate!!
    # else:
    #     print(f"Sorry, that's wrong. Final Score: {score}")
