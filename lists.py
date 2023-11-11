states_of_US=["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
               "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina",
                 "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi",
                   "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa",
                     "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska",
                       "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
                         "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
copy_states=states_of_US.copy()
states_of_US.append("Punjab")
print(f"appends Punjab to end of list \n {states_of_US}")
#Add an item to the end of the list. Equivalent to a[len(a):] = [x].
iterable=["Delhi"]

states_of_US.extend(iterable)
print(f"extend the list by adding another list to end of current list \n{states_of_US}")
#Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

states_of_US.insert(51, "Haryana")
print(f"inserts a value at 51 or x given position of list \n {states_of_US}")
#Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

states_of_US.remove("Punjab")
#Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
print(f"removes the first occurence of element in the list \n {states_of_US}")

x=states_of_US.pop()
#Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)
print(f"removes the items at given position in the list in this case 51 and returns the removed element \n {x}")

states_of_US.clear()
#Remove all items from the list. Equivalent to del a[:].
print(f"clear removes all items of the list \n {states_of_US}")

states_of_US=copy_states
states_of_US.index("Utah",20,53)
print(f"returns the index of the value passed in index in between start and end which are optional \n {states_of_US}")
#Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

#The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

x=states_of_US.count("Haryana")
print(f"returns the numnber of times the value passed in count appears in the list \n {x}")
#Return the number of times x appears in the list.

states_of_US.sort( key=len, reverse=False) # sorts the list based on length of them and reverese false means ascending and true means descending
#Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).
print(f"returns the sorted list based on key which is custom and liek key can be lenght of each element \n {states_of_US}")

states_of_US.reverse()
#Reverse the elements of the list in place.
print(f"revereses the list \n {states_of_US}")

states_of_US.copy()
print(states_of_US)
