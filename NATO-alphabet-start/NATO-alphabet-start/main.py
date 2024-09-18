student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
name_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")



phonetic_alphabet={row.letter:row.code for (index, row) in name_data_frame.iterrows()}
    #pass
#print(phonetic_alphabet)
#phonetic_name=[code for(letter,code) in phonetic_alphabet.items() if letter in nameletters]


#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
userInputAlphabet=True
while userInputAlphabet:
    try:
        userName=input("Enter your name ")
        userName=userName.upper()
        phonetic_name=[phonetic_alphabet[letter] for letter in userName]
    except Exception as e:
        print(f"only alphabets should be in the name {e}")
    else:
        print(phonetic_name)
        userInputAlphabet=False
        
        
