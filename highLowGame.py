from gameData import data
from art import highLow, vs, over
import random

print(highLow)



def formatData(account):
    return f"{account["name"]} a {account["description"]} from {account["country"]}"
    #print()

#while playon:
#print(f"Is {accountA["name"]} who is {accountA["description"]} from {accountA["country"]}")

def gameview(accountI, accountJ):
    testA=formatData(accountI)
    print(testA)
    print("\n")
    print(vs)
    print("\n")
    testB=formatData(accountJ)
    print(testB)
    print("\n")

def userWon(person1, person2):
    person1=person2
    person2=random.choice(data)
    while person1==person2:
            person2=random.choice(data)
    return person1, person2


def letsPlayGame():
    
    playon=True
    count=0
    accountA=random.choice(data)
    accountB=random.choice(data) 
    while accountB==accountA:
            accountB=random.choice(data)
    gameview(accountA, accountB)
    while playon:
        
        
        #print(accountA)
        
        userAnswer=input("who has more followers? Type 'A' or 'B' ")
        if userAnswer.upper()=="A" and accountA["follower_count"]>accountB["follower_count"]:
            accountA, accountB=userWon(accountA, accountB)
            gameview(accountA, accountB)
            count+=1
            print(f"your current score is {count}")
        elif userAnswer.upper()=="B" and accountA["follower_count"]<accountB["follower_count"]:
            accountA, accountB=userWon(accountB, accountA)
            gameview(accountA, accountB)
            count+=1
            print(f"your current score is {count}")
        else:
            print(f"You Lost \n {over}")
            
            exit()

letsPlayGame()
          



