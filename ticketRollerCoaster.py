print("welcome to roller coaster ticketing booth")
height=int(input("what is your height in cm"))
if height <= 120:
    print("you are not allowed to ride the roller coaster")
else:
    print("you are allowed to ride the roller coaster")
    print(f"price of one ticket for adult is 20 \n price of one ticket for children is 15 \n price of one ticket for senior is 13")
    ticketsRequired=int(input("how many tickets you want? "))
    adultTickets=int(input("how many adult tickets? "))
    seniorTickets=int(input("how many senior tickets? "))
    childrenTickets=int(input("how many children tickets? "))
    #totalPriceOfTickets=20*adultTickets+15*childrenTickets+13*seniorTickets
    print(f"your total is {20*adultTickets+15*childrenTickets+13*seniorTickets}$")
    