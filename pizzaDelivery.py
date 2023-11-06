print("Thank you for choosing Python Pizza Deliveries!")
small_pizza=15
medium_pizza=20
large_pizza=25
pepperoni_small=2
pepperoni_med_large=3
extraCheese=1
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
if size == "S":
  if add_pepperoni == "Y" and extra_cheese == "Y":
    print(f"Your final bill is: ${small_pizza+pepperoni_small+extraCheese}.")
  elif add_pepperoni == "N" and extra_cheese == "Y":
    print(f"Your final bill is: ${small_pizza+extraCheese}.")
  elif add_pepperoni == "Y" and extra_cheese == "N":
    print(f"Your final bill is: ${small_pizza+pepperoni_small}.")
  elif add_pepperoni == "N" and extra_cheese == "N":
    print(f"Your final bill is: ${small_pizza}.")
if size == "M":
  if add_pepperoni == "Y" and extra_cheese == "Y":
    print(f"Your final bill is: ${medium_pizza+pepperoni_med_large+extraCheese}.")
  elif add_pepperoni == "N" and extra_cheese == "Y":
    print(f"Your final bill is: ${medium_pizza+extraCheese}.")
  elif add_pepperoni == "Y" and extra_cheese == "N":
    print(f"Your final bill is: ${medium_pizza+pepperoni_med_large}.")
  elif add_pepperoni == "N" and extra_cheese == "N":
    print(f"Your final bill is: ${medium_pizza}.")
if size == "L":
  if add_pepperoni == "Y" and extra_cheese == "Y":
    print(f"Your final bill is: ${large_pizza+pepperoni_med_large+extraCheese}.")
  elif add_pepperoni == "N" and extra_cheese == "Y":
    print(f"Your final bill is: ${large_pizza+extraCheese}.")
  elif add_pepperoni == "Y" and extra_cheese == "N":
    print(f"Your final bill is: ${large_pizza+pepperoni_med_large}.")
  elif add_pepperoni == "N" and extra_cheese == "N":
    print(f"Your final bill is: ${large_pizza}.") 