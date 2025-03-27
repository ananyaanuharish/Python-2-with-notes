# Day 7 Notes
 #! 1. Exception Handling in Python.
 # Its a way to deal with errors in your code so it doesn’t crash the program.
 # You use special keywords link:
 # try: Put the code that might cause an error.
 # except: What to do if there is an error.
 # finally: Optional, for code that should run no matter what.
 
 #! 2. Let's understand Exception Handling as cookies analogy.
 # Start Cooking: Begin making biryani (like starting your program).
 # Problem Occurs: Run out of salt (an error occurs in the process).
 # Handle Exception: Borrow salt or buy more (handle the error to continue).
 # Continue Cooking: Finish making biryani successfully (program runs without crashing).
 
 #! 3. Example of try except finally
try:
     # Taking inputs and performing division
     num1 = int(input("Enter the numerator: "))
     num2 = int(input("Enter the denominator: "))
     result = num1 / num2
except Exception as e:
     print(f"An error occurred: {e}")
else:
     print(f"The result of {num1} divided by {num2} is: {result}")
finally:
     print("Execution completed.")
 
 #! 4. Multiple Exceptions.
 # Specific Responses.
 # Improved Debugging.
 # Better User Experience.
 
 #! 5. Example with Built-in Exceptions.
 # ZeroDivisionError: Raised when dividing by zero.
 # ValueError: Raised when a function gets the right type but an invalid value.
 # TypeError: Raised when an operation is applied to an object of an inappropriate type.
 # IndexError: Raised when trying to access an index that is out of range in a list or tuple.
 # Extras: FileNotFoundError: Raised when a file or directory is requested but doesn’t exist.
 
try:
     # Input two numbers and perform division
     num1 = int(input("Enter the numerator: "))
     num2 = int(input("Enter the denominator: "))
 
     # Performing division
     result = num1 / num2
 
     # Example of possible IndexError
     sample_list = [1, 2, 3, "4"]
     index = int(input("Enter an index to access in the list [1, 2, 3, 4]: "))
     value = sample_list[index]  # Accessing list element
 
except ZeroDivisionError:
     print("Error: Division by zero is not allowed.")
except ValueError:
     print("Error: Please enter valid integers.")
except IndexError:
     print("Error: Index out of range. Please enter a valid index between 0 and 2.")
except TypeError:
     print("Error: Type mismatch. Cannot concatenate string and number.")
else:
     print(f"The result of {num1} divided by {num2} is: {result}")
     print(f"Accessed value at index {index} is: {value}")
finally:
     print("Execution completed.")
 
 #! 6. Example with FileNotFoundError exception.
try:
     file=open("example.txt","r")
     # Some code that might raise an exception
except FileNotFoundError:
     print("File not found!")
finally:
     file.close()
     print("File closed.")
 
 #! 7. Why Not Just Fix Errors?
 # Unpredictable Inputs.
 # External Factors.
 # Graceful Handling. (Seamless Error Handling.)