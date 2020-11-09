# Lets have a look at some built in functions in Python

# Import is the key word we use to call modules from Python library

# Random method from the python library used by importing
import random
import math

# Generates a float number between 1.0 - 0.0
print(random.random())
print("=" * 40)

###########################

num_float = 23.80
print("Floor method rounds the figure to lower end -----> i.e. 23 ")
print(math.floor(num_float))
print("=" * 40)

#############################
print("Ceil method rounds the figure to higher end ------> i.e. 24")
print(math.ceil(num_float))
print("=" * 40)

##############################

# Task
# Get user input of a float number
# Check if the number is greater than .50 then round the figure to lower end
# Check if the number is greater than .51 then round the figure to higher end
# Example. num_float = 23.66 - round it to 24.

user_float = float(input("Please input a float number\n -> "))

if user_float % 1 < .5:
    output = math.floor(user_float)
else:
    output = math.ceil(user_float)

print(f"Formatted number: {output}")