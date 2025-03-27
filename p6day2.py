# 1. if else based on weather condition

weather_condition = 'cold'
if(weather_condition == 'rainny'):
    print("do not go outside")
elif(weather_condition=='sunny'):
    print("go outside and play")
elif(weather_condition=='cold'):
    print("Wear jacket and go")
else:
    print("invalid input")

# 2. looping through a list
fruits=["apple","banana","orange"]

# 2.1. Looping all data using for loop
for f in fruits:
    print(f)

# 2.2. Looping all data using for loop but till a specific range
for f in range(2):
    print(fruits[f])

# 2.3 Loop through keys and values
person_1={"name":"ananya","age":"22","gender":"female"}
for key,values in person_1.items():
    print(f"{key} : {values}")
