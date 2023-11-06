print("welcome to roller coaster ticketing booth")
adultfare=20
childrenfare=15
seniorfare=13
photofare=3
height=int(input("what is your height in cm "))
if height <= 120:
    print("you are not allowed to ride the roller coaster")
else:
    print("you are allowed to ride the roller coaster")
    phototaken=input("do you want photo to be taken? \n the price of photo is 3$ each \n Y or N \n")
    totalTicketsRequired=int(input("how many total tickets you want? "))
    if totalTicketsRequired == 1:
        age=int(input("what is your age? "))
        if age>=18 and phototaken == "Y":
            #print(f"price of one ticket for adult is 20$")
            print(f"your total is {photofare+adultfare}$")
        elif age>=18 and phototaken == "N":
            print(f"your total is {adultfare}$")
        elif age < 18 and phototaken == "Y":
            print(f"your total is {photofare+childrenfare}$")
        elif age<18 and phototaken == "N":
            print(f"your total is {childrenfare}$")
        elif 45<=age<=55 and phototaken == "Y":
            print(f"everything is going to be alright and have a free ride on us! and your total on photo is {photofare}") #mide life crisis
        elif 45<=age<=55 and phototaken == "N":
            print(f"everything is going to be alright and have a free ride on us!") #mide life crisis
        elif age>=60 and phototaken == "Y":
            print(f"your total is {photofare+seniorfare}$")
        elif age>=18 and phototaken == "N":
            print(f"your total is {seniorfare}$")
            
        
    elif totalTicketsRequired > 1 and phototaken == "Y":
        print(f"price of one ticket for adult is 20 \n price of one ticket for children is 15 \n price of one ticket for senior is 13")
        childrenTickets=int(input("do you want any children tickets, \n if yes then how many would you want \n the age of children has to be less than 12 ? "))
        seniorTickets=int(input("do  you want any senior tickets? \n if yes then how many would you want? \n the age of senior has to be greater than 60? "))
        adultTickets=int(input("do  you want any adult tickets? \n if yes then how many would you want? \n the age of adult is 18 or greater "))

        #print(f"price of one ticket for adult is 20 \n price of one ticket for children is 15 \n price of one ticket for senior is 13")

        #adultTickets=int(input("how many adult tickets? "))
        #seniorTickets=int(input("how many senior tickets? "))
        #childrenTickets=int(input("how many children tickets? "))
        #totalPriceOfTickets=20*adultTickets+15*childrenTickets+13*seniorTickets
        print(f"your total is {adultfare*adultTickets+childrenfare*childrenTickets+seniorfare*seniorTickets+totalTicketsRequired*photofare}$")
    elif totalTicketsRequired > 1 and phototaken == "N":
        print(f"price of one ticket for adult is 20 \n price of one ticket for children is 15 \n price of one ticket for senior is 13")
        childrenTickets=int(input("do you want any children tickets, \n if yes then how many would you want \n the age of children has to be less than 12 ? "))
        seniorTickets=int(input("do  you want any senior tickets? \n if yes then how many would you want? \n the age of senior has to be greater than 60? "))
        adultTickets=int(input("do  you want any adult tickets? \n if yes then how many would you want? \n the age of adult is 18 or greater "))

        #print(f"price of one ticket for adult is 20 \n price of one ticket for children is 15 \n price of one ticket for senior is 13")

        #adultTickets=int(input("how many adult tickets? "))
        #seniorTickets=int(input("how many senior tickets? "))
        #childrenTickets=int(input("how many children tickets? "))
        #totalPriceOfTickets=20*adultTickets+15*childrenTickets+13*seniorTickets
        print(f"your total is {adultfare*adultTickets+childrenfare*childrenTickets+seniorfare*seniorTickets}$")
    