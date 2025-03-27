import os
os.system('cls')
# 1. What are Data Structures?
# It's a way to store and organize data in a computer's memory.

# 2. Why we use Data Structures?
# To store and manage data efficiently and safely.

# 3. What are some common data structures in Python?
# Lists, Tuples, Dictionaries, Sets

# 3. What is a list?
# A list is a collection of ordered, changeable(mutable), and indexed data elements.
# It allow duplicate elements, and you can store different types of data in a single list. (integers, strings, and duplicate values only)

# 4. How do you create a list in Python?
my_list = [1, 2, 3, "apple", "banana", 3]

# 5. Let's understand list with Indian analogy
# There is an Indian Thali with different types of food, same goes for the list.

# 6. Some common operations in the list

# 6.1. access the list
print(my_list[3])

# 6.2. Append (Insert value at the end of the list)
my_list.append("mango")
print(my_list)


# 6.3. Insert (Insert value at specific index)
my_list.insert(1, "orange")
print(my_list)

# 6.4. Remove (Remove value from the list by value)
my_list.remove(3)
print(my_list)

# 6.5. Pop (Update value at specific index)
my_list.pop(1)
print(my_list)

