# to do now :)
import random
from art import logo
import os
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
want_continue = True

def calculate_score(cand_cards):
    score = sum(cand_cards)
    if score > 21 and 11 in cand_cards:
        cand_cards.remove(11)
        cand_cards.append(1)
    return score

def asking_user_choice():
    user_choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if user_choice == 'y':
        c3 = random.choice(cards)
        user_cards.append(c3)
        # user_cards_sum = sum(user_cards)
        # if user_cards_sum > 21 and c3 == 11:
        #     user_cards.remove(c3)
        #     c3 = 1
        #     user_cards.append(c3)
        print(f"Your cards: {user_cards}, final score: {calculate_score(user_cards)}")
        if calculate_score(user_cards) > 21:
            print(f"Computer's final hand: {comp_cards}, final score: {calculate_score(comp_cards)}")
            print("You lose")
        elif calculate_score(user_cards) == 21:
            print(f"Blackjack! You win!")
        else:
            asking_user_choice()
    else:
        # print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
        # # cc2 = random.choice(cards)
        # # comp_cards.append(cc2)
        # print(f"Computer's final hand: {comp_cards}, final score: {calculate_score(comp_cards)}")
        print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")

        # Dealer draws until reaching 17
        while calculate_score(comp_cards) < 17:
            comp_cards.append(random.choice(cards))

        print(f"Computer's final hand: {comp_cards}, final score: {calculate_score(comp_cards)}")

        # comp_cards_sum = sum(comp_cards)
        # user_cards_sum = sum(user_cards)
        if calculate_score(comp_cards) > 21:
            print("Opponent went over. You win!")
        elif calculate_score(comp_cards) == 21:
            print(f"Blackjack! Dealer win!")
        elif calculate_score(comp_cards) == calculate_score(user_cards):
            print("Its draw")
        elif calculate_score(comp_cards) > calculate_score(user_cards):
            print("You lose")
        # elif calculate_score(comp_cards) < calculate_score(user_cards):
        #     print("You win!")
        # elif comp_cards_sum == user_cards_sum:
        #     print("Its draw")
        # elif comp_cards_sum > user_cards_sum:
        #     print("You lose")
        # elif comp_cards_sum < user_cards_sum:
        #     print("You win")
        else:
            asking_user_choice()

while want_continue:
    user_agree = input("Do you want to play a game of BlackJack?" \
    "Type 'y' or 'n': ").lower()
    if user_agree == 'y':
        os.system("cls")
        print(logo)
    else:
        break

    # have to give 2 cards to user 
    user_cards = []
    comp_cards = []
    c1 = random.choice(cards)
    c2 = random.choice(cards)
    user_cards.append(c1)
    user_cards.append(c2)
    print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")

    # one card for computer
    cc1 = random.choice(cards)
    cc2 = random.choice(cards) # not shown to user
    comp_cards.append(cc1)
    print(f"Computer's first card: {cc1}")
    comp_cards.append(cc2) # later added to list for sum

    # Check immediate blackjack condition before asking for hits
    if calculate_score(user_cards) == 21 and calculate_score(comp_cards) == 21:
        print(f"Your cards: {user_cards}, final score: {calculate_score(user_cards)}")
        print(f"Computer's cards: {comp_cards}, final score: {calculate_score(comp_cards)}")
        print("Both have Blackjack! It's a draw!")
        continue   # Start next round

    elif calculate_score(user_cards) == 21:
        print(f"Your cards: {user_cards}, final score: {calculate_score(user_cards)}")
        print(f"Computer's cards: {comp_cards}, final score: {calculate_score(comp_cards)}")
        print("Blackjack! You win!")
        continue

    elif calculate_score(comp_cards) == 21:
        print(f"Your cards: {user_cards}, final score: {calculate_score(user_cards)}")
        print(f"Computer's cards: {comp_cards}, final score: {calculate_score(comp_cards)}")
        print("Blackjack! Dealer wins!")
        continue

    # asking user
    asking_user_choice()
    # user_choice = input("Type 'y' to get another card, type 'n' to pass:").lower()
    # if user_choice == 'y':
    #     c3 = random.choice(cards)
    #     user_cards.append(c3)
    #     user_cards_sum = sum(user_cards)
    #     print(f"Your cards: {user_cards}, final score: {sum(user_cards)}")
    #     if user_cards_sum > 21:
    #         print(f"Computer's final hand: {comp_cards}, final score: {sum(comp_cards)}")
    #         print("You lose")
    #     else:


    # cc2 = random.choice(cards)
    # comp_cards.append(cc2)
    # print(f"Computer's cards: {comp_cards}")
    # comp_cards_sum = sum(comp_cards)

