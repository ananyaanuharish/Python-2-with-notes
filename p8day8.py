import os
os.system('cls')
#! 1. What is Object-Oriented Programming (OOP)? 
# It is a way of writing code using classes and objects to represent real-world things.
# It helps organize code into reusable parts, making it easier to build and manage programs.
 
#! 2. There are four main pillars of OOP that we will cover in detail:
# Class: A template to create objects.
# Object: An instance of a class with its own data.
# Inheritance: Allows one class to use the properties of another.
# Encapsulation: Hides data to protect it.
# Polymorphism: Lets objects use the same method in different ways.

#! 4. What is a Class in OOP?
# It is a blueprint or template for creating objects in programming.
# It defines the attributes (data) and methods (functions) that describe the behavior and properties of the objects created from it.
# It allows you to create multiple objects (instances) with shared attributes and behaviors, defined by a common template.
 
#! 5. What is an Object?
# An object is a unique instance of a class with its own attribute values and can perform behaviors defined by the class.

#! 6. Indian Thali Analogy for OOP:
# Recipe (Class):
# The recipe acts as a blueprint that defines the ingredients and preparation methods, similar to how a class defines attributes and behaviors for objects.
 
# Thali (Object):
# The thali is the actual meal prepared using the recipe, but each thali can have variations (e.g., different side dishes or plating), just like objects created from a class have unique attribute values.

#! 7. Basic example of OOP:
 #* 7.1. Define a class named 'Car'
class Car:
     # Constructor method to initialize attributes when a new object is created
     def __init__(self, color, model):       # Special __init__ method with 'self' as the first parameter
         self.color = color                  # Assign the value of 'color' to the object's 'color' attribute
         self.model = model                  # Assign the value of 'model' to the object's 'model' attribute
 
     # Method to start the car and print a message
     def start(self):                         # 'self' refers to the instance calling this method
         print(f"{self.model} is starting.")  # Print a message including the car's model
 
 # Example usage
car1 = Car("Red", "Sedan")                   # Create an instance of the Car class with color 'Red' and model 'Sedan'
car1.start() 

#! Extras:
 # The __init__ method is a special method in Python used to initialize newly created objects.
 # If you want to avoid using __init__, you can create a custom initialization method, such as set_attributes, to initialize the attributes manually after creating the object.
 
 #* 7.2. Define a class named 'Car' without using the __init__ constructor
class Car:
     # Custom method to set attributes for the Car object
     def set_attributes(self, color, model):  # Takes 'color' and 'model' as parameters
         self.color = color                   # Assign the value of 'color' to the object's 'color' attribute
         self.model = model                   # Assign the value of 'model' to the object's 'model' attribute
 
     # Method to start the car and print a message
     def start(self):                         # 'self' refers to the instance calling this method
         print(f"{self.model} is starting.")  # Print a message including the car's model
 
 # Example usage
car1 = Car()                                 # Create an object of the 'Car' class without initial attributes
car1.set_attributes("Red", "Sedan")           # Use the custom method to set attributes for 'car1' object
car1.start() 

#! 8. What is Inheritance?
 # What is Inheritance?
 # Inheritance allows one class to inherit the properties and methods of another class.
 # This helps in reusing code and creating a hierarchy of classes.
 
 #* 8.1. Mechanism:
 # Allows one class to inherit properties and methods from another class.
 
 #* 8.2. Code Reuse:
 # Enables the reuse of attributes and behaviors from the parent class in child classes.
 
 #* 8.3. Hierarchy:
 # Establishes a class hierarchy where child classes extend or specialize the parent class.
 
 # Parent class definition
class Animal:
     # Method in the parent class
     def speak(self):                      # 'self' refers to the current object instance
         print("Animal is making a sound")  # Default sound for any generic animal
 
 # Child class definition that inherits from Animal
class Dog(Animal):                        # 'Dog' is a subclass of 'Animal'
     # Overriding the 'speak' method of the parent class
     def speak(self):                      # 'self' refers to the Dog object instance
         print("Dog is barking")           # Custom behavior for Dog
 
 # Creating an object of the child class 'Dog'
my_dog = Dog()                            # Create an instance of Dog class
my_dog.speak()  

#! 11. Multiple vs Single Inheritance:
 #* 11.1 Multiple Inheritance:
 # A class inherits from multiple parent classes, combining features from all parents.
 #  Example: Supported in Python.
 
 #^ Example of Multiple Inheritance:
 # Parent class 1
class Vehicle:
     def features(self):
         print("Vehicle has wheels and an engine.")
 
 # Parent class 2
class Machine:
     def machine_type(self):
         print("This is a mechanical machine.")
 
 # Child class inheriting from both Vehicle and Machine
class Car(Vehicle, Machine):
     def car_info(self):
         print("Car is a type of vehicle and machine.")
 
 # Creating an object of the Car class
car = Car()
car.features()         # Output: Vehicle has wheels and an engine.
car.machine_type()     # Output: This is a mechanical machine.
car.car_info()         # Output: Car is a type of vehicle and machine. 

#! 13. What is Encapsulation?
 #* 13.1. Bundling
 # Group related data and methods together inside a class.
 
 #* 13.2. Data Hiding
 # Restrict direct access to internal attributes, making them private to protect data integrity.
 
 #* 13.3. Control
 # Use getter and setter methods to manage how data is accessed and modified safely.
 
 #! 14. There are 2 types of Encapsulation:
 # Private vs Public: 
 #* 14.1. Private
 # Attributes and methods are accessible only within the class (e.g., _attr or __attr).
 
 #* 14.2. Public
 # Attributes and methods are accessible from outside the class and can be freely modified.

 #! 15. Example of Encapsulation with proper comments:
 # BankAccount class definition to manage a bank account
class BankAccount:
     def __init__(self, initial_balance=0):  # Constructor with an optional initial balance parameter
         self.__balance = initial_balance    # Private attribute: __balance is hidden from direct access
 
     # Public method to deposit money into the account
     def deposit(self, amount):
         if amount > 0:                     # Check if the deposit amount is positive
             self.__balance += amount        # Increment the balance by the deposit amount
             print(f"Deposited: {amount}")   # Display the deposited amount
         else:
             print("Deposit amount must be positive!")  # Error message for invalid deposit amounts
 
     # Public method to withdraw money from the account
     def withdraw(self, amount):
         if 0 < amount <= self.__balance:    # Check if the withdrawal amount is positive and less than or equal to the balance
             self.__balance -= amount        # Decrease the balance by the withdrawal amount
             print(f"Withdrew: {amount}")    # Display the withdrawn amount
         else:
             print("Insufficient balance or invalid amount.")  # Error message for insufficient balance or invalid withdrawal amounts
 
     # Public method to view the current balance (getter method)
     def get_balance(self):
         return self.__balance               # Return the current balance safely
 
 # Example usage of the BankAccount class
account = BankAccount(1000)                 # Create a BankAccount object with an initial balance of 1000
account.deposit(500)                        # Deposit 500 into the account; Output: Deposited: 500
account.withdraw(200)                       # Withdraw 200 from the account; Output: Withdrew: 200
print(f"Balance: {account.get_balance()}")  # Display the current balance; Output: Balance: 1300
print(account.__balance)                    # This will cause an AttributeError because __balance is private
 
 #* 15.1. Practical Use Case:
 # In a real-world banking application, using private attributes (Balance) with public methods (Deposit, Withdraw, and GetBalance) ensures:
 # Security: The balance cannot be directly altered by anyone.
 # Controlled Access: Only specific methods can change the balance.
 # Data Integrity: Prevents invalid operations like withdrawing more money than available.
 
# 16. Getters and Setters:
 # Getters and setters are methods used to access and modify the private attributes of a class.
 
 #^ Example
 # Class definition with private attributes and getters/setters
class Student:
     def __init__(self, name, grade):
         self.__name = name                # Private attribute for name
         self.__grade = grade              # Private attribute for grade
 
     # Getter for name
     def get_name(self):
         return self.__name                # Retrieve private name attribute
 
     # Setter for name
     def set_name(self, name):
         if isinstance(name, str):         # Check if name is a string
             self.__name = name
         else:
             print("Invalid name. Please enter a valid string.")
 
     # Getter for grade
     def get_grade(self):
         return self.__grade               # Retrieve private grade attribute
 
     # Setter for grade
     def set_grade(self, grade):
         if 0 <= grade <= 100:             # Validate grade (must be between 0 and 100)
             self.__grade = grade
         else:
             print("Invalid grade. Must be between 0 and 100.")
 
 # Example usage
student1 = Student("Alice", 85)           # Create a Student object
 
 # Using getter methods
print(student1.get_name())                # Output: Alice
print(student1.get_grade())               # Output: 85
 
 # Using setter methods
student1.set_name("Bob")                  # Change the name to Bob
student1.set_grade(95)                    # Change the grade to 95
 
 # Access the updated values using getters
print(student1.get_name())                # Output: Bob
print(student1.get_grade())               # Output: 95

#! 17. What is Polymorphism?
 # Polymorphism allows different classes to be treated as if they are instances of the same class through a common interface.
 # The term means "many forms" — a single method or operation can behave differently based on the object calling it.
 
 #* 17.1. Method Overriding:
class Bird:
     def sound(self):
         print("Some generic bird sound")
 
class Sparrow(Bird):
     def sound(self):
         print("Chirp Chirp")  # Sparrow's version of the sound method
 
class Eagle(Bird):
     def sound(self):
         print("Screech")  # Eagle's version of the sound method
 
 # Using polymorphism
birds = [Sparrow(), Eagle()]  # List of different bird objects
for bird in birds:
     bird.sound()  # Output: Chirp Chirp (for Sparrow), Screech (for Eagle)

#! 18. What is Abstraction?
 # Abstraction is the process of hiding the complex implementation details and showing only the essential features of an object.
 # It focuses on what an object does rather than how it does it.
 
 #! 19. Why use Abstraction?
 # Enforces a Structure: Makes sure all subclasses have the required methods, keeping code consistent.
 # Defines a Blueprint: Creates a template for child classes to follow, so they all have a similar structure.
 # Prevents Instantiation: Abstract classes cannot be used directly to create objects, so developers must create specific subclasses.
 
 #! 20 Example of Abstraction: (Abstract Class)
from abc import ABC, abstractmethod  # Importing the Abstract Base Class (ABC) and abstractmethod from the 'abc' module
 # ABC stands for Abstract Base Class.
 # abstractmethod is a decorator that is applied to methods in an abstract class.
 
 # Abstract class definition
class Animal(ABC):  # Animal is an abstract base class that cannot be instantiated
     @abstractmethod
     def sound(self):  # Abstract method with no implementation, serves as a template for subclasses
         pass          # 'pass' is used because this method has no concrete implementation
 
 # Concrete class 1: Dog inherits from Animal
class Dog(Animal):
     def sound(self):  # Implementing the abstract method 'sound' in Dog class
         print("Bark")  # Custom behavior for Dog class
 
 # Concrete class 2: Cat inherits from Animal
class Cat(Animal):
     def sound(self):  # Implementing the abstract method 'sound' in Cat class
         print("Meow")  # Custom behavior for Cat class
 
 # Creating objects and using the method
dog = Dog()  # Creating an instance of the Dog class
cat = Cat()  # Creating an instance of the Cat class
 
 # Calling the 'sound' method on the instances
dog.sound()  # Output: Bark (Dog class's implementation of the sound method)
cat.sound()  # Output: Meow (Cat class's implementation of the sound method) 