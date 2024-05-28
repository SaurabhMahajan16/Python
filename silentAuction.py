from art import gavelArt, auction
import os
import json

print (auction)


bidderList=[]


def addBidder():
    os.system('cls||clear')    
    name= input("what is your name: ")
    bid=int(input("what price you want to bid: "))

    bids={
        "name":name,
        "bid": bid
    }
    bidderList.append(bids)
    print("Yes if there are more bidders \n No if there are no more bidders ")
    moreBids=input()
    moreBids=moreBids.lower()
    
    if moreBids=="yes":
        os.system('cls||clear')
        addBidder()
    elif moreBids=="no":
        compareBids(bidderList)
    else:
        print("you have not entered yes or no")
        print("do you want to continue type yes else tyoe anything to terminate")
        goOn=input().lower()
        if goOn=="yes":
            os.system('cls||clear')
            addBidder()
        else:
            print("exiting the program")
            exit

    
def compareBids(bidList):
    numberOfBids=len(bidList)
    maximumbid=0
    maximumBidName=""
    for list in range(0, numberOfBids):
        if bidList[list]["bid"]>maximumbid:
            maximumbid=bidList[list]["bid"]
            maximumBidName=bidList[list]["name"]

    print(gavelArt)    
    print(f" \n silent auction is won by {maximumBidName} and the bid is {maximumbid}")
    print(json.dumps(bidList, indent=2))

addBidder()




 


    
    