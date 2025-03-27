file = open("python 1.txt","w") #to create a file
print(file)

file = open("Python 2.txt","r") #to read a file
print(file)

#appending to a file
file = open("example.txt","a")
file.write("\nthus is a new line.")
file.close()