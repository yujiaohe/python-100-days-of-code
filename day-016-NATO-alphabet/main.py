# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas as pd
# 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
phonetic_df = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {rows.letter: rows.code for _, rows in phonetic_df.iterrows()}
# print(alpha_dict)
# 2. Create a list of the phonetic code words from a word that the user inputs.
user = input("Enter a word: ").upper()
result = [phonetic_dict[letter] for letter in user]
print(result)