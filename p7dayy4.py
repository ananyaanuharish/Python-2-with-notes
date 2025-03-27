import os
os.system('cls')
# 7. What are Tuples?
# A tuple is a collection of ordered, and indexed data elements. But the twist is that, tuples are immutable.
# It means that, once tuple is created, you cannot change, add, or remove items from it.
# Tuples are useful when you want to ensure that the data remains constant throughout the program.

# 8. How do you create a list in Python?
my_tuple = (1, 2, 3, "apple", "banana", 3)

# 9. Let's understand tuples with Indian analogy
# Once a train ticket is booked, then, you cannot change the PNR/Seat Number

# 10. Some common operations in the tuple

# 10.1. Access the tuple
print(my_tuple[3])

# 10.2. Count (Count the number of occurrences of a value in the tuple)
print(my_tuple.count(3))

# 10.3. Index (Find the index of a value in the tuple)
print(my_tuple.index("apple"))

# 10.4. Len (Get the length of the tuple)
print(len(my_tuple))

# 11. Where are tuples used in real programming world?
# Tuples are used when you want to store and manipulate a collection of data that should not be changed throughout the program.

# 12. What are Dictionaries?
# A dictionary is a collection of unordered, mutable, and unique key-value pairs. Each key is unique, and it is used to access the corresponding value.
# It allows different types of values but doesn't allow duplicate keys in a single dictionary.


# 13. How do you create a dictionary in Python?
my_dict = {
    "apple": "a fruit", 
    "book": "a collection of pages", 
    "car": "a vehicle",
    "age": 30
}

# 14. Let's understand dictionary with Indian analogy
# A person's identity card, which contains information like name, age, address, etc.

# 15. Common operations in the dictionary

# 15.1. Access the dictionary
print(my_dict["age"])

# 15.2. Add new key-value pair
my_dict["color"] = "red"
print(my_dict)

# 15.3. Remove key-value pair
my_dict.pop("car")
print(my_dict)

# 15.4. Dictionary Properties and Methods
print(len(my_dict))  # Get the number of items
print(my_dict.keys())  # Get a list of all keys
print(my_dict.values())  # Get a list of all values
print(my_dict.items())  # Get a list of all key-value pairs

# 15.5. Merge Two Dictionaries
my_dict.update({"city": "New York"})
print(my_dict)

# 15.7  Copy a Dictionary
my_dict2 = my_dict.copy()
print(my_dict2)

# 15.6. Clear the Dictionary
my_dict.clear()
print(my_dict)

# 16. Where are dictionaries used in real programming world?
# Dictionaries are used when you want to store and manipulate a collection of data that needs to be organized and accessed by a key-value pair.
# Like a real life dictionary.

# 17. What are Sets?
# A set is a collection of unordered, mutable, and unique elements.
# It allows different types of values but doesn't allow duplicate values in a single set.
# Duplicate values are automatically removed when a set is created.

# 18. How do you create a set in Python? (With duplicated value)
my_set = {1, 2, 3, "apple", "banana", 3}
print(my_set)

# 19. Let's understand set with Indian analogy
# A group of friends.

# 20. Common operations in the set

# 20.1. Go through each item in the set using a loop and print it
for item in my_set:
    print(item)

# 20.2. Convert set to a list for indexing
my_list = list(my_set)
print(my_list[0])

# 20.3. Check if an item exists in the set
if "apple" in my_set:
    print("Apple is in the set")

# Note: Adding or removing elements in a set may result in a different order each time, as sets manage positions internally.

# 20.4. Add new item to the set
my_set.add("orange")
print(my_set)

# 20.5. Remove item from the set
my_set.remove("banana")
print(my_set)

# 20.6. Clear the set
my_set.clear()

# 21. So why to use sets as the result may vary after each run?
# Uniqueness: Removes duplicates automatically.  
# Fast lookup for an item: Quickly checks item existence.  
# Efficient Operations: Supports union, intersection, and difference.

# 22. When to use which Data Structure type?
# Lists: Use when you need an ordered collection that can be changed. Example: shopping list.
# Tuples: Use when you need an ordered collection that should not change. Example: days of the week.
# Dictionaries: Use when you need to connect a unique key to a value. Example: mapping names to ages.
# Sets: Use when you need a collection with no duplicates. Example: list of unique colors. 

# 23. Extras: (Union, intersection, and difference.)

# 23.1 Union: Combines all unique elements from both sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))  # Output: {1, 2, 3, 4, 5}

# 23.2 Returns elements common to both sets.
print(set1.intersection(set2))  # Output: {3}

# 23.3 Returns elements present in set1 but not in set2.
print(set1.difference(set2))  # Output: {1, 2}

# 23.4 Returns elements present in either set1 or set2 but not in both.
print(set1.symmetric_difference(set2))  # Output: {1, 2, 4, 5}

# os.system('cls')
# # 24. How the data is stored in real life.
# x = [
#     { "name":"Raj", "age": 20, "city": "Delhi" },
#     { "name":"Rahul", "age": 21, "city": "Mumbai" },
#     { "name":"Ravi", "age": 22, "city": "Chennai" },
#     { "name":"Rajesh", "age": 23, "city": "Kolkata" }
# ]