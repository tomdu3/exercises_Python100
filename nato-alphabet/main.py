import pandas as pd

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
file_data = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in file_data.iterrows()}
nato_spell = []

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

while True:
    user_word = input("What word would you like to NATO spell? : ").upper()
    try:
        # for character in user_word:
        #     nato_spell.append(nato_dict[character])
        nato_spell = [nato_dict[character] for character in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet, please.")
    else:
        break
print(nato_spell)