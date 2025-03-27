import os

#! 1. What is File Handling?
# File handling is the process of opening, reading, writing, deleting, and closing files in a program.

#! 2. Why do we need to handle files in Python?
# We handle files to store data permanently and to perform
# various operations like reading and updating on the data.

#! 3. Understanding File Handling Using a Notebook Analogy
# Open the notebook to read what’s inside.
# Write new information on a blank page.
# Append new information at the end of the notebook if there’s already something written.
# Close the notebook when you’re done.

#! 4. How do you create & open a file in Python?
# The open() function is used to open a file in Python.
# It takes two arguments: the file path and the mode in which the file should be opened.

# Example:
file = open("example.txt", "w") # To create a file
file = open("example.txt", "r") # To read a file

#! 5. What are the different modes of creating/opening a file in Python?
# The different modes of opening a file in Python are:
# "w": Write mode. (Creates a new file or rewrite an existing file.)
# "r": Read mode. (If file don't exist, then, it will throw an error.)
# "a": Append mode. (creates a new file if the file doesn’t exist, otherwise it appends to the existing file.)
# "r+": Read and write mode. (It will not create a file, if it don't exist.)

#! 6. Let's understand this by the Library Analogy.
# Think of a file like a book in a library. When you open a book.
# "w": You create a new book with blank pages, if already exist, it will get deleted.
# "r": You open an existing book for reading, but you can't make any changes.
# "a": If book don't exist by mistake, create new book, else you open an existing book for adding new content at the end.
# "r+": You open an existing book, where you can add new pages at the end of the book withouterasing the existing content.

#! 7 Reading a file.
# The read() method is used to read the entire content of a file.

#^ 7.1 Reading the entire file:
file = open("example.txt", "r") # Open the file in read mode
contents = file.read() # Read the entire content of the file
print(contents) # Print the content
file.close() # Close the file

#* Note: You must close file at the end to free up the system resources. Specially RAM.

#^ 7.2 Reading the entire file:
file=open("example.txt","r")
for line in file:
    print(line)
file.close()

#* This method is useful when you’re dealing with large files and don’t want to load the entirecontent into memory at once.

#! 8. Writing to a file.
# The write() method is used to write content to a file.
# If the file doesn’t exist, it creates a new file, else overwrite the file with the new data.

file=open("example.txt","w")
file.write("Hello, World!")
file.close()

#! 9. Appending to a file.
# The append() method is used to add content to an existing file.
# If the file doesn’t exist, it creates a new file, else it will append the data in the end.

file=open("example.txt","a")
file.write("\nThis is a new line.")
file.close()

#! 10. Closing a file.
# The close() method is used to close an open file.
# It is important to close the file after performing any operations on it,
# as it frees up system resources and prevents potential data loss.

#! 11 Check if the file exists before deleting.
# Let's learn how to delete a file using Python.

file_path = "example.txt"
if os.path.exists(file_path):
    os.remove(file_path)  # Delete the file
    print(f"{file_path} has been deleted successfully.")
else:
    print(f"{file_path} does not exist.")

#! 12. All modes in Python.
# "w": Write mode (creates a new file or rewrite an existing file).
# "r": Read mode (default mode), if file don't exist, then, it will throw an error.
# "a": Append mode (creates a new file if the file doesn’t exist, otherwise it appends to the existing file).
# "r+": Read and write mode.
#! Extras 
# "x": Exclusive creation mode (creates a new file, fails if the file already exists)
# "b": Binary mode (used for non-text files)

# Example:
with open("example.txt", "r") as file:
    # Perform operations on the file
    contents = file.read()
    print(contents)

#! 13. Writing Programs to Creating, Appending, and Summing Numbers from a File.
# Create and write initial sample numbers to the file
file = open("data.txt", "w")
file.write("1\n2\n3\n4\n")  # Add some numbers, each on a new line
file.close()  # Close the file after writing

# Append more numbers to the file
file = open("data.txt", "a")  # Open in append mode
file.write("5\n6\n7\n")  # Append numbers, each on a new line
file.close()  # Close the file after appending

# Open the file in read mode and calculate the total sum
file = open("data.txt", "r")
total = 0  # Starting total
for line in file:
    if line.strip():  # Ensure the line is not empty
        total += int(line.strip())  # Convert each line to an integer and add to total
file.close()  # Close the file after reading

# Print the sum of numbers
print("The sum of the numbers is:", total)

#! 14. Understanding Pyton Modules, & Libraries.
# A module is a file containing Python code, while a library is a collection of modules.

#* 14.1 Popular Python Libraries.
# "math": Provides functions for mathematical operations like sqrt(), sin(), cos(), etc.
# "random": Generates random numbers.
# "os": Interacts with the operating system, such as reading or writing files.
# "sys": Provides access to system-specific parameters and functions.
# "time": Handles time-related operations.
# "datetime": Works with dates and times.

#* 14.2 How to import a library.
import os
import math

#* 14.3 File Paths and Directories (Extras).
# os.path: Manage and manipulate file and directory paths.
# os.listdir(): Retrieve a list of files and directories in a given path.
# os.mkdir(): Create a new directory at the specified path.

#! 15. Try-Except block.
# The try-except block is used to handle exceptions in Python.
# It allows you to define a block of code to be tested for exceptions,
# and a block of code to be executed if an exception occurs.

#* 15.1. Check file existence using Python Library and Handling Errors

import os
filename ="example.txt"
try:
    if os.path.exists(filename):
        file=open(filename,"r")
        print(file.read())
        file.close()
    else:
        print(f"The file {filename} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

#! 16. Working wit CSV Files:
# You can use proper structures CSV files for large data handling, ans
# efficient data storage and retrieval.

#* 16.1. Reading CSV Files
import csv
with open('example.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)  # Prints each row as a list

# * 16.2. Writing to CSV Files
import csv
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'London'],
    ['Charlie', 35, 'Paris']
]
with open('output.csv', mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)  # Writes multiple rows at once

#! 16.3 Extras.
# csv.reader: Reads CSV file line-by-line as a list of strings.
# csv.writer: Writes rows of data into a CSV file.
# newline='': Prevents blank lines when writing on Windows systems.
# Even you can use pandas library for efficiency.

#! 17. We can do same for json too, but will do this in further session.
#* Here are some core functions of json module.
# json.load(): Reads from a file and converts JSON data into a Python object.
# json.dump(): Writes a Python object to a file in JSON format.
# json.loads(): Parses a JSON string into a Python object.
# json.dumps(): Converts a Python object into a JSON string.

#! 18. File Compression.
# Python also provides inbuilt file compression for zip, gzip, & tarfile.
# This can be useful for storing large files or sending them over the network.

#* 18.1. Importing all the compression modules.
import zipfile    # Work with ZIP archives
import gzip       # Compress/decompress individual files
import tarfile    # Handle TAR archives


#! 16. Conclusion.
# CRUD-C.
# Use Python libraries like os to interact with the file system.
# Must use try-except blocks for every function.