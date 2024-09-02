#weeklyWeather=[]
#with open ("weather_data.csv", "r") as weatherReport:
#    weatherData=weatherReport.readlines()
#    print(weatherData)
#    
#    for data in weatherData:
#        data=data.strip("\n")
#        weeklyWeather.append(data)
#    print(weeklyWeather)
import csv
import pandas
from statistics import mean

with open("weather_data.csv") as weatherReport:
    #data=csv.reader(weatherReport)
    #temperature=[]
    #for line in data:
    #    if line[1]!="temp":
    #        temperature.append(int(line[1]))
    #print(temperature)
    
    data=pandas.read_csv("weather_data.csv")
    dictData=data.to_dict()
    print(dictData)
    print(pandas.DataFrame.from_dict(dictData))
    tempList=data['temp'].to_list()
    print(tempList)
    print(f"average weekly Temperature: {data['temp'].mean()}")
    print(f"hottest week Temperature: {data['temp'].max()}")
    print(f"the highest tempature was on \n{data[data.temp==data['temp'].max()]}")
    monday=data[data.day=="Monday"]
    print((monday.temp*9/5)+32)
    
data = {'index': [('a', 'b'), ('a', 'c')],
        'columns': [('x', 1), ('y', 2)],
        'data': [[1, 3], [2, 4]],
        'index_names': ['n1', 'n2'],
        'column_names': ['z1', 'z2']}
print(pandas.DataFrame.from_dict(data))

# making data frame 
#data = pandas.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv") 
#    
## calling head() method  
## storing in new variable 
#data_top = data.head() 
#fullData = data.to_dict()
## display 
#print() 
#print(pandas.DataFrame.from_dict(fullData, orient='index'))
