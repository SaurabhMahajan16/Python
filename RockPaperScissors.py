import random

print("\n "+ "\n"+"\n")
print('''$$\   $$\ $$$$$$$$\ $$\       $$\       $$$$$$\    
$$ |  $$ |$$  _____|$$ |      $$ |     $$  __$$\   
$$ |  $$ |$$ |      $$ |      $$ |     $$ /  $$ |  
$$$$$$$$ |$$$$$\    $$ |      $$ |     $$ |  $$ |  
$$  __$$ |$$  __|   $$ |      $$ |     $$ |  $$ |  
$$ |  $$ |$$ |      $$ |      $$ |     $$ |  $$ |  
$$ |  $$ |$$$$$$$$\ $$$$$$$$\ $$$$$$$$\ $$$$$$  |  
\__|  \__|\________|\________|\________|\______/  ''')

print("\n "+ "\n"+"\n")

print("Lets play rock paper scissors")

print("\n "+ "\n"+"\n")

userChoice=int(input("what do you like to choose? Type 0 for rock, 1 for paper or 2 for scissors  \n\n "))



rock=''' 
"!!!THAT'S IT, MAN!!! KEEP THROWING THAT
HEAVY SHIT AT ME!!! THAT HEAVY SHIT!!!"   _____
        \                              /\| | | |
         \                            / /|_|_|_|
          \                           \        |
            (  ( ) ) ( )  )            \_______/
           ( ( ( ( )  )  ) )           /______/
          ( ( )) ) (   ) ( ( )        /       /
          ( (__.-.___.-.__) )        /       /
          / ---._.---._.---\        /       /
          \||    '/  '   ||/       /       /
            |||  (_     |||       /       /
             || ///\\\  ||\______/       /
        ___/ ||||\__/|||||/             /
       /   \   ||||||||  /             /
      /     \   ||||||  /        _____/
'''

namePaper='''                                                          
8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
88                     88                                 
88                     88                                '''

paper='''     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)'''

nameScissors='''               d8b                                        
                Y8P                                        
                                                           
.d8888b  .d8888b888.d8888b .d8888b  .d88b. 888d888.d8888b  
88K     d88P"   88888K     88K     d88""88b888P"  88K      
"Y8888b.888     888"Y8888b."Y8888b.888  888888    "Y8888b. 
     X88Y88b.   888     X88     X88Y88..88P888         X88 
 88888P' "Y8888P888 88888P' 88888P' "Y88P" 888     88888P' '''
scissors='''   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

#print(rock+"\n "+ "\n"+"\n"+namePaper+"\n"+"\n"+paper+"\n "+ "\n"+"\n"+nameScissors+"\n"+"\n"+scissors+"\n "+ "\n"+"\n")

rockValue=0
scissorsValue=2
paperValue=1

computerChoice=random.randint(0,2)

if userChoice == rockValue:
    if computerChoice == paperValue:
        print(f"computer chooses paper \n\n {paper} and \n\n you loose !!!!!! \n\n {rock}")
    elif computerChoice == rockValue:
        print(f"you both chooses rock, no results its a tie!!!!! \n\n {rock}\n\n{rock}")
    elif computerChoice == scissorsValue:
        print(f"you win \n {rock} \n\n as computer chose scissors \n{scissors}")

elif userChoice == paperValue:
    if computerChoice == rockValue:
        print(f"You win !!!!! computer chooses rock \n \n {rock} \n\n and you choose{paper}")
    elif computerChoice == paperValue:
        print(f"you both chooses paper, no results its a tie \n \n {paper}\n \n {paper}")
    elif computerChoice == scissorsValue:
        print(f"you loose!!!! \n \n {paper} \n\n as computer chose scissors \n \n {scissors}")

elif userChoice == scissorsValue:
    if computerChoice == rockValue:
        print(f"You loose !!!!! computer chooses rock \n\n {rock} \n\n and you choose scissors \n\n{scissors}")
    elif computerChoice == paperValue:
        print(f"you win!!! computer chooses paper \n\n {paper} \n\n  you chose \n\n {scissors}")
    elif computerChoice == scissorsValue:
        print(f"you both chooses scissors, no results its a tie!!!! \n\n {scissors}\n\n {scissors}")

#print(computerChoice)