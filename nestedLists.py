fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])
dirtyfruitsVeggies=input("enter dirty dozen \n")
n=12
dirtyfruitsVeggies=dirtyfruitsVeggies.strip().split()[:n]# to take input as a list and then convert them to individual elements
print(dirtyfruitsVeggies)