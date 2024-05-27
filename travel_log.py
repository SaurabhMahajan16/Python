country = input("Add country name: ") # Add country name
visits = int(input("Number of visits: ")) # Number of visits
number_of_cities=int(input("number of cities visited: "))
list_of_cities = [] # create list from formatted string
print("name of cities: ")
for city in range(0,number_of_cities):
    city_visited=input()
    list_of_cities.append(city_visited)

print(list_of_cities)
travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(country, visits, cities_list):
  log={"country": country, "visits": visits, "cities": list_of_cities}
  travel_log.append(log)
  #print(travel_log)
    


# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")