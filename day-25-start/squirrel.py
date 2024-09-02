import pandas as pd

data=pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240830.csv")
blackCount=len(data[data["Primary Fur Color"]=="Black"])

greyCount=len(data[data["Primary Fur Color"]=="Gray"])
cinnamonCount=len(data[data["Primary Fur Color"]=="Cinnamon"])
#for line in data:
#    
#    if line["Primary Fur Color"]== "Gray":
#        greyCount+=1
#    elif line["Primary Fur Color"]== "Cinnamon":
#        cinnamonCount+=1
#    elif line["Primary Fur Color"]== "Red":
#        blackCount+=1
#
print(f"grey count is {greyCount} \nblack count is {blackCount} \ncinnamon count is {cinnamonCount}")
data_dict={
    "Fur Color":["black", "Cinnamon", "Gray" ],
    "Count":[blackCount, cinnamonCount, greyCount]
}
df=pd.DataFrame.from_dict(data_dict)
df.to_csv("Squirrels_Color_Count")