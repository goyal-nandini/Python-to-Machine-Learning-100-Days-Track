import random
import hangman_art
import hangman_words

random_word = random.choice(hangman_words.word_list)

print(random_word) # for debugging

# guess = input("Enter a letter:\n").lower()

def create_display(word):
    lst = []
    for _ in word:
        lst.append("_")
    return lst

display = create_display(random_word)

print("".join(display)) # shows to user to guess this number of word size

lives = 6
guessed_letters = set()   # EDGE CASE 
while '_' in display:
    guess = input("Enter a letter:\n").strip().lower()
     # EDGE CASE: Empty input
    if guess == "":
        print("Input cannot be empty.")
        continue

    # EDGE CASE: More than one character
    if len(guess) != 1:
        print("Please enter only ONE letter.")
        continue

    # EDGE CASE: Non-alphabetic
    if not guess.isalpha():
        print("Please enter a valid letter (a–z).")
        continue

    # EDGE CASE: Repeated guess
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.add(guess)

    found = False

    # check the entire word
    for ind, letter in enumerate(random_word):  # 🤔👇
        if guess == letter:
            display[ind] = guess
            found = True
            # 💥 problem is how do i stop printing this stage 3 times if s is 3 times in session
            # print(hangman_stages.stages[lives])
            # print(lives)
    
    # print stages only once 💥
    if found:
        print(hangman_art.stages[lives])
    if not found: # this means "!false" means "true" -> if condition m true ho tabhi vo exceute hoti hai :)
        print("Wrong input") # this is shown when it type wrong letter
        print(hangman_art.stages[lives-1])
        lives -= 1
        print(lives)

    if lives == 0:
        print("Game Over, You lose!!")
        break
    print("".join(display)) # show user the updated word with correct guess letters


# if not found:
#     print("Wrong input")

# print("".join(display)) # show user the updated word with correct guess letters

'''🤔 What is enumerate()?

enumerate() is a Python function that gives you index + value while looping.

Normally, if you loop like this:

for letter in random_word:
    print(letter)


You only get the letter, NOT the index.

But for Hangman, you also need the position to update the display list.

That's where enumerate() helps.'''
