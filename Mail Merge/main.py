PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as file: # u can skip ./ as u(main.py) are in same directory as Input
    name = file.readlines() # its a list with \n(new line character)
    print(name)

with open("./Input/Letters/starting_letter.txt") as file: # u can skip ./
    letter_content = file.read() # imp step :)
    for n in name:
        new_n = n.strip()
        new_letter = letter_content.replace(PLACEHOLDER, new_n)
        print(new_letter)
        with open(f"./Output//ReadyToSend/letter_for_{new_n}.txt", mode="w") as completed_letters:
            completed_letters.write(new_letter)
