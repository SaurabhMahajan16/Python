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
    for deck in range (0,7):
        for i in range(2,12):
            cards.append(i)

    print(cards)
    return cards

def clearScreen():
    os.system('cls||clear')

##def dealerCards(deck):
 #   print("dealer Deck")
 #   dealerDeck=[]
 #   dealerdeck=random.choice(deck)
 #   return dealerdeck

def getCards(cardDeck):
    newDeck=[]
    newDeck.append(int(random.choice(cardDeck)))
    newDeck.append(int(random.choice(cardDeck)))
    return newDeck

def getanotherCard(deck,currentDeck):
    newDeck=currentDeck
    newDeck.append(int(random.choice(deck)))
    #print(newDeck)
    return newDeck


def getCard(deck):
    return random.choice(deck)
    
def whoWon(dealer, gambler):
    if dealer>gambler and dealer<=21:
        return "You Lost"
    elif dealer< gambler and gambler <=21:
        return "You Won"    
    elif dealer>21:
        return "You Won"
    elif gambler>21:
        return "You Lost"

def doubleBett(deck, player, dealer):
    newgamblerDeck=getanotherCard(deck, player)
    print(f" your new deck is {newgamblerDeck}")
    newdealerDeck=getanotherCard(deck, dealer)
    print(f"dealers new deck is {newdealerDeck}")
    newgamblerCardsTotal=sum(newgamblerDeck)
    newdealerCardsTotal=sum(newdealerDeck)
    winner=whoWon(newdealerCardsTotal,newgamblerCardsTotal) 
    print(f"{blackJackLogo} \n\n\n {winner}")


deckOfCard=cardDeck()

#gamblers=createGmabelers()
dealerDeck=[]
#deckOfdealer=dealerDeck(deckOfCard)
gamblerCards=getCards(deckOfCard)
print(f"gamblers cards are {gamblerCards}")
dealerCards=getCards(deckOfCard)
print(f"dealers cards are {dealerCards}")
gamblerCardsTotal=sum(gamblerCards)

dealerCardsTotal=sum(dealerCards)
blackJack=21
game_over=True
while game_over:
    winner= whoWon(dealerCardsTotal, gamblerCardsTotal)
    print(f"{blackJackLogo} \t\n\n\n {winner} ")
    #if dealerCardsTotal==blackJack:
    #    print("\n\nYou lost from dealer\n\n")
    #    game_over=False
#
    #if gamblerCardsTotal>blackJack:
    #    print(f"{blackJackLogo} \n\n\n You lost")
    #    game_over=False
    #
    #if dealerCardsTotal>blackJack:
    #    print(f"{blackJackLogo} You Won")
    #    game_over=False
#
    #
    #elif dealerCardsTotal<gamblerCardsTotal and gamblerCardsTotal<=blackJack:
    #    print(f"{blackJackLogo} You Won")
    doubleBet=input("do you want to double your bet for black Jack Y or N ")
    #if doubleBet.upper()!="Y" or doubleBet.upper()!="N":
    #    print("if you answer Y then will double the bet else it will exit")
    #    doubleBet=input()
    if doubleBet.upper()=="Y":
            doubleBett(deckOfCard,gamblerCards,dealerCards)
            game_over=False
    else:
            game_over=False

    #elif dealerCardsTotal>gamblerCardsTotal and dealerCardsTotal<blackJack:
    #    print("do you want to double your bet for black Jack Y or N ")
    #    doubleBet=input()
    #    if doubleBet.upper()=="Y":
    #            doubleBett(deckOfCard,gamblerCards,dealerCards)
    #            game_over=False
    #    else:
    #            game_over=False










#print(gamblers)


