from art import coffee
from CoffeeMenu import MENU, RESOURCES
import os

print(coffee)

def getReport():
    print(f"water = {resources['water']} ml \nmilk = {resources['milk']} ml\ncoffee = {resources['coffee']} gm")

def getInput():
    want=input("What would you like?(espresso/late/cappucino): ").lower()
    #print(want)
    return want

def checkResources(new_resources):
    for item in new_resources:
        if new_resources[item]>resources[item]:
            print("not enough resources")
            return False
    return True

    print("resources left")
    #return True

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def makeCoffee(drink, orderIngridients):
    for item in orderIngridients:
        resources[item]-=orderIngridients[item]

    print(f"your drink is {drink}")
    #return resources

def askForMoney(coffee):
    print("Please insert coins")
    pennies=int(input("number of pennies"))
    dimes=int(input("number o cents"))
    nickels=int(input("number o nickels"))
    quarters=int(input("number of quarters"))
    totalmoney=[pennies+dimes*10+nickels*5+quarters*25]
    if totalmoney==MENU[coffee]["cost"]: 
        return True
    elif totalmoney>MENU[coffee]["cost"]:
        change=(totalmoney-int(MENU[coffee]["cost"]))/100
        print(f"your change is {change}")
        return True
    else:
        print("Sorry that's not enough money!! Please collect your money!")




    
coffee=True

while coffee:
    userInput=getInput().lower()
    if userInput=="report":
        getReport()
    elif userInput=="off":
        coffee=False
        exit()
    else:
        drinkOrdered=MENU[userInput]
        
        if checkResources(drinkOrdered["ingredients"]):
            if askForMoney(userInput):
                makeCoffee(userInput, drinkOrdered["ingredients"])
    #if userInput=="latte":
    #    if checkResources(userInput):
    #        if askForMoney(userInput):
    #            makeCoffee(userInput, MENU[userInput]["ingredients"])
    #if userInput=="espresso":
    #    if checkResources(userInput):
    #        if askForMoney(userInput):
    #            makeCoffee(userInput, MENU[userInput]["ingredients"])



#print(MENU["espresso"]["ingredients"])