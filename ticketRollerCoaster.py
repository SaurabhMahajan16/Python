print("welcome to roller coaster ticketing booth")
height=int(input("what is your height in cm "))
if height <= 120:
    print("you are not allowed to ride the roller coaster")
else:
    print("you are allowed to ride the roller coaster")
    totalTicketsRequired=int(input("how many total tickets you want? "))
    if totalTicketsRequired == 1:
        age=int(input("what is your age? "))
        if age>=18:
            print(f"price of one ticket for adult is 20$")
            
            
        elif age < 18:
            print(f"price of one ticket for children is 15$")
            
        elif age>=60:
            print(f"price of one ticket for senior is 13")
            
        #ticketsRequired=int(input("how many adult tickets you want? "))
    elif totalTicketsRequired > 1:
        print(f"price of one ticket for adult is 20 \n price of one ticket for children is 15 \n price of one ticket for senior is 13")
        childrenTickets=int(input("do you want any children tickets, \n if yes then how many would you want \n the age of children has to be less than 12 ? "))
        seniorTickets=int(input("do  you want any senior tickets? \n if yes then how many would you want? \n the age of senior has to be greater than 60? "))
        adultTickets=int(input("do  you want any adult tickets? \n if yes then how many would you want? \n the age of adult is 18 or greater "))

        #print(f"price of one ticket for adult is 20 \n price of one ticket for children is 15 \n price of one ticket for senior is 13")

        #adultTickets=int(input("how many adult tickets? "))
        #seniorTickets=int(input("how many senior tickets? "))
        #childrenTickets=int(input("how many children tickets? "))
        #totalPriceOfTickets=20*adultTickets+15*childrenTickets+13*seniorTickets
        print(f"your total is {20*adultTickets+15*childrenTickets+13*seniorTickets}$")
    