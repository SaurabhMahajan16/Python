from gameData import data
from art import highLow, vs, over
import random
import os

print(highLow)



def formatData(account):
    return f"{account["name"]} a {account["description"]} from {account["country"]}"
    #print()

#while playon:
#print(f"Is {accountA["name"]} who is {accountA["description"]} from {accountA["country"]}")

def gameview(accountI, accountJ):
    testA=formatData(accountI)
    print(f"Compare A: {testA}")
    #print("\n")
    print(vs)
    #print("\n")
    testB=formatData(accountJ)
    print(f"Against B: {testB}")
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
            os.system('cls||clear')
            gameview(accountA, accountB)
            count+=1
            print(f"You're right! Current score: {count}")
        elif userAnswer.upper()=="B" and accountA["follower_count"]<accountB["follower_count"]:
            accountA, accountB=userWon(accountA, accountB)
            os.system('cls||clear')
            gameview(accountA, accountB)
            count+=1
            print(f"You're right! Current score: {count}")
        else:
            print(highLow)
            print(f"Sorry, that's wrong. Final score: {count}\n{over}")
            
            exit()

letsPlayGame()
          



