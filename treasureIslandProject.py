print('''
       
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
******************************************************************************* 

''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction=input('You are at a cross road where do you want to go? type \"right" or "left" \n')
direction_lower=direction.lower()
if direction_lower=="left":
    choice1=input('You came to the lake thereis an island in the middle of the lake.\n Type \"wait" to wait for a boat \n or \n Type "swim" to swim across \n')
    choice1_lower=choice1.lower()

    if choice1_lower=="wait":
        color_choice=input('You have arrived at the island unharmed. \n There is a house with 3 doors. One red, one yellow and one blue. \n Which color do you like to choose? \n Type the color name below \n')
        color_choice_lower=color_choice.lower()
        if color_choice_lower=="red":
            print("Game over! You are burned by the fire")
        elif color_choice_lower=="blue":
            print("Game over! You are eaten by the beasts")
        elif color_choice_lower=="yellow":
            print("You won the game, this is your chest below")
            print(r'''   
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
''')
        else:
            print("You choose wrong, Game Over!!!")
    elif choice1_lower=="swim":
        print("You have been attacked by the trout, Game Over!!!")
    else:
        print("You choose wrong, Game Over!!!!")
else:
    print("You fell into a hole, Game over!!!!")
