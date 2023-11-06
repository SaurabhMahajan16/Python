print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_name=name1+name2
lower_name=combined_name.lower()
t=lower_name.count("t")
t+=lower_name.count("r")
t+=lower_name.count("u")
t+=lower_name.count("e")
l=lower_name.count("l")
l+=lower_name.count("o")
l+=lower_name.count("v")
l+=lower_name.count("e")
value=str(t)+str(l)
score=int(value)
if score<10 or score>90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif 40<score<50:
    print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")






