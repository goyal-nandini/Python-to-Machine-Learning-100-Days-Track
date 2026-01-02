# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index, row) in nato_df.iterrows()}
print(nato_dict)

user_name = input("What is you name? ").upper()
user_name_list = [nato_dict[letter] for letter in user_name]
print(user_name_list)
