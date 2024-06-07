from art import blackJackLogo
import random
import os

#blackJack=True

def createGmabelers():
    numberOfPersons=int(input("number of persons playing balckjack : "))
    gambler=[]
    for persons in range(1,numberOfPersons+1):
        #print(numberOfPersons)
        gambler.append("gambler"+str(persons))
    return gambler

def cardDeck():
    cards=[]
    for deck in range (0,4):
        for i in range(2,12):
            cards.append(i)

    print(cards)
    return cards

def clearScreen():
    os.system('cls||clear')

def dealerCards(deck):
    print("dealer Deck")
    dealerDeck=[]
    dealerdeck=random.choice(deck)
    return dealerdeck

def getCards(cardDeck):
    newDeck=[]
    newDeck.append(int(random.choice(cardDeck)))
    newDeck.append(int(random.choice(cardDeck)))
    return newDeck

def getanotherCard(deck,currentDeck):
    return currentDeck.append(int(random.choice(deck)))


def getCard(deck):
    return random.choice(deck)
    
    



deckOfCard=cardDeck()

gamblers=createGmabelers()
dealerDeck=[]
#deckOfdealer=dealerDeck(deckOfCard)
gamblerCards=getCards(deckOfCard)
dealerCards=getCards(deckOfCard)
gamblerCardsTotal=sum(gamblerCards)
dealerCardsTotal=sum(dealerCards)
blackJack=21
if dealerCardsTotal==blackJack:
    print("\n\nYou lost from dealer\n\n")
elif dealerCardsTotal<gamblerCardsTotal and gamblerCardsTotal<blackJack:
    print(f"{blackJackLogo} You Won")
    doubleBet=input("do you want to double your bet for black Jack Y or N")
    if doubleBet!="Y" or doubleBet!="N":
        print("if you answer Y then will double the bet else it will exit")
        doubleBet=input()
        if doubleBet.lower()=="Y":
            gamblerCardsTotal=sum(getanotherCard(deckOfCard, gamblerCards))
            dealerCardsTotal=sum(getanotherCard(deckOfCard, dealerCards))
            if 









#print(gamblers)


