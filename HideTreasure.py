line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? Type A1,A2,A3 \n or \n B1,B2,B3 \n or \n C1,C2,C3 \n").lower() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
#positionMarker=position[0]
#print(positionMarker)
list=['a','b','c']
marker=list.index(position[0])
numeric=int(position[1])-1
#print(marker)
if numeric==0:
  if marker==0:
    line1[marker]='X'
  elif marker==1:
    line1[marker]='X'
  elif marker==2:
    line1[marker]='X'
elif numeric==1:
  if marker==0:
    line2[marker]='X'
  elif marker==1:
    line2[marker]='X'
  elif marker==2:
    line2[marker]='X'
elif numeric==2:
  if marker==0:
    line3[marker]='X'
  elif marker==1:
    line3[marker]='X'
  elif marker==2:
    line3[marker]='X'

#print(marker)

#print(position)

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")