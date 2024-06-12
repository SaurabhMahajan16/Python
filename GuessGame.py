from art import guessingGame, win, lose
import random

print(guessingGame)
playGame=True
high="\t too high"
low="\t too low"
hardChances=5
easyChances=10
won="win"
#def guessHardNumber(guess, real):
# if guess<real:
#  print(low)
# elif guess>real:
#  print(high)
# elif guess==real:
#  print(win)


 

def guessNumberGame(guess, real):
 if guess<real:
  return low
 elif guess>real:
  return high
 elif guess==real:
  return won

def youWin(chances, outcome):
 if outcome==won:
    print(win)
    quit()
 elif chances==9 and outcome!=won:
  print(f"you lose \n\n\n\n {lose}")
  print(f"the real number was {number} ")
  quit()
 
 

guessGame=True
number=int(random.randint(0,100))
level=input("choose your level \t")

 
 
 
test=0
match level.lower():
 case "hard":
  print(" you have 5 chances")
  while test<5:
   guessNumber=int(input(" guess the number \t"))
   result=guessNumberGame(guessNumber,number)
   print(result)
   test+=1
   youWin(4,result)
   print(f"you have {5-test} chances left")
   
 
 
 case "easy":
  print("you have 10 chances")
  while test<10:
   guessNumber=int(input(" guess the number \t"))
   result=guessNumberGame(guessNumber,number)
   print(result)
   test+=1
   youWin(9,result)
   print(f"you have {10-test} chances left")
   
   

    
  