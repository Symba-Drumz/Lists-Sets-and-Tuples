# collection = single variable used to store multiple values
# List = [] ordered and changeable, duplicates allowed.
# Sets = {} unordered and unindexed, no duplicates allowed.
# Tuple = () ordered and unchangeable, duplicates allowed.

#LISTS
cymbals = ["Zildjian", "Sabian", "Meinl", "Paiste", "Istanbul"]
print(cymbals)
#Accessing elements in a list
print(cymbals[0])  # Zildjian . This helps us access the first element of the list
print(cymbals[-1])  # Istanbul
print(cymbals[3:-1])# Paiste only excluding Istanbul
print(cymbals[3:6])  # Paiste, Istanbul
print(cymbals[::2]) # Zildjian, Meinl, Istanbul, starts from 0 and skips every second element.
print(cymbals[::-1]) # Istanbul, Paiste, Meinl, Sabian, Zildjian, reverse the list

print(dir(cymbals))  # shows all the methods available for the list object.
print(len(cymbals))  # returns the number of elements in the list
print("Zildjian" in cymbals)  # returns True if Zildjian is in the list. in is a membership operator confirming if the element is in the list. Returns False if not in the list

#Iterating through a list
for cymbal in cymbals:
    print(cymbal)  # prints each element in the list

#Changing elements in a list
cymbals[3]  = "Soultone"  
print(cymbals)  # ['Zildjian', 'Sabian', 'Meinl', 'Soultone', 'Istanbul'] Soultone replaced Paiste

#Adding elements to a list at the end
cymbals.append("Paiste")  # adds Paiste to the end of the list
print(cymbals)  # ['Zildjian', 'Sabian', 'Meinl', 'Soultone', 'Istanbul', 'Paiste']

#Removing elements from a list
cymbals.remove("Soultone")
print(cymbals)  # ['Zildjian', 'Sabian', 'Meinl', 'Istanbul', 'Paiste'] Soultone removed from the list

#Inserting a new value at a specific index
cymbals.insert(2, "Soultone")  # inserts Soultone at index 2
print(cymbals)  # ['Zildjian', 'Sabian', 'Soultone', 'Meinl', 'Istanbul', 'Paiste']

#Sorting a list
cymbals.sort()  # sorts the list in ascending order
print(cymbals)

#Reversing a list
cymbals.reverse()  # reverses the list
print(cymbals)  # ['Zildjian', 'Sabian', 'Soultone', 'Meinl', 'Istanbul', 'Paiste']

#Removing everything from a list
#cymbals.clear()  # removes all elements from the list( I wont print this out now lol!)   

#Finding the index of an element
print(cymbals.index("Zildjian")) # returns the index of Zildjian in the list

#Finding the count of an element
print(cymbals.count("Zildjian")) # returns the count of Zildjian in the list

#Copying a list
cymbals2 = cymbals.copy()  # creates a copy of the list
print(cymbals2)  # ['Zildjian', 'Sabian', 'Soultone', 'Meinl', 'Istanbul', 'Paiste']


# SETS
# sets are unordered and unindexed, no duplicates allowed. They are faster than lists.
# You cannot change the elements of a set since sets dont have indexes but you can add or remove elements.
# You cannot have mutable elements in a set like lists or dictionaries. You can only have immutable elements like strings, numbers, and tuples.
fruits = {"apple", "banana", "cherry", "apple"}  # sets are unordered and unindexed, no duplicates allowed
print(fruits)  # {'banana', 'cherry', 'apple'} apple is only printed once

fruits.add("orange")  # adds orange to the set
print(fruits)

fruits.remove("banana")  # removes banana from the set
print(fruits)  # {'cherry', 'apple', 'orange'}banana removed from the set

print("banana" in fruits) # returns True if banana is in the set. in is a membership operator confirming if the element is in the set. Returns False if not in the set

fruits.pop()  # removes a random element from the set
print(fruits)  # {'apple', 'orange'} random element removed from the set
#fruits.clear()  # removes all elements from the set

print(dir(fruits))  # shows all the methods available for the set object.
print(len(fruits))  # returns the number of elements in the set.

vegetables = {"carrot", "broccoli", "spinach"}
print(vegetables)  # {'carrot', 'broccoli', 'spinach'}
# Union of two sets
grocery_list = fruits.union(vegetables) # combines both sets
print(grocery_list)  # {'carrot', 'broccoli', 'spinach', 'apple', 'orange'}
    

for fruit in fruits: # iterating through a set  
    print(fruit)


# TUPLES
# tuples are ordered and unchangeable, duplicates allowed.. They are faster than lists and sets.
sticks = ("Vic Firth", "ProMark", "Zildjian", "Vater", "Regal Tip")
print(sticks)  # ('Vic Firth', 'ProMark', 'Zildjian', 'Vater', 'Regal Tip')

print(dir(sticks))  # shows all the methods available for the tuple object.
print(len(sticks))  # returns the number of elements in the tuple.Returns 5
print(sticks.index("Vater")) # returns the index of Vater in the tuple. Returns 3
print(sticks.count("Vater")) # returns the count of Vater in the tuple. Returns 1
print("Vic Firth" in sticks) # returns True if Vic Firth is in the tuple. in is a membership operator confirming if the element is in the tuple. Returns False if not in the tuple.
print(sticks[0])  # Vic Firth: this helps us access the first element of the tuple.

for stick in sticks: # iterating through a tuple
    print(stick)