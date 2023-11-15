import random
from hangman_arts import stages, logo
from hangman_word_list import word_list

print(f'''
      \n\n\n {logo}
      \n\n\n\

''')

choosen_word=random.choice(word_list)
print(f"choosen word is \n {choosen_word} \n")
total_spaces=len(choosen_word)
blank_spaces=""
for i in range(0, total_spaces):
    blank_spaces+="_"

print(f"Number of spaces in the word are : \n\n\n\n {blank_spaces}\n\n")
print("please guess a letter \n\n")
print(f"you have {total_spaces} guesses if you made {total_spaces} wrong guesses you will loose the game")

end_of_game=True
lives=6
while end_of_game:

    letter_guessed=input("guess any letter : \n")
    if not letter_guessed.isalpha():
        print("you have not entered an alphabet, please enter an alphabet!!!!")
    elif letter_guessed.isalpha():
        letter_guessed=letter_guessed.lower()
        answer=choosen_word.count(letter_guessed)



    
    #answer=
        if answer>=1:
            print(f"you guessed right \n\n {letter_guessed}")
            guessed_index=choosen_word.index(letter_guessed)
            #print(f"your index is {choosen_word.index(letter_guessed)}")
            if letter_guessed in blank_spaces:
                print(f"You have already guessed the letter, Please choose another letter {modify_spaces} !!")


            #print(guessed_index)
            blank_spaces=list(blank_spaces)
            #states_of_US.insert(51, "Haryana")
            blank_spaces[guessed_index]=letter_guessed
            modify_spaces=" ".join(blank_spaces)
            print(modify_spaces)



        else:
            print(f"you lost a life")

            lives-=1
            print(f"{stages[lives]}")
            if lives==0:
                end_of_game=False
                print(f"ohhhh!!!!!!!!!! you loose the game")

        if blank_spaces.count("_") ==0:
            end_of_game=False
            print(f"YAAAYYYYYYY You got it right!!!!!!")
            print(f"you have won the game!!!!!!")

    