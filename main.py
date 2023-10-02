import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data.letter)

# for index, row in data.iterrows():
#     print(row.letter)

# Creating a dictionary from 'data' DataFrame
nato_dict = {row.letter: row.code for index, row in data.iterrows()}
# print(nato_dict)

is_game = True
while is_game:
    user_input = input("What's your name: ").upper()

    user_letter = [letter for letter in user_input]
    try:
        user_list = [nato_dict[nato_alphabet] for nato_alphabet in user_letter]
    except KeyError:
        print("Sorry only letters please")
    else:
        print(user_list)
        is_game = False
