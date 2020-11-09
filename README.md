# Modules
- Built in functions
- Python Library
- What is pip and how to use it
- APIs with Python 

- Built in functions help us accelerate our
development of software 
```python
# Lets have a look at some built in functions in Python

# Import is the key word we use to call modules from Python library

# Random method from the python library used by importing
import random
import math

# Generates a float number between 1.0 - 0.0
print(random.random())
print("=" * 40)

################################################

num_float = 23.80
print("Floor method rounds the figure to lower end -----> i.e. 23 ")
print(math.floor(num_float))
print("=" * 40)

################################################
print("Ceil method rounds the figure to higher end ------> i.e. 24")
print(math.ceil(num_float))
print("=" * 40)

################################################
```
### Task - using floor and ceil functions
```python
# Get user input of a float number
# Check if the number is greater than .50 then round the figure to lower end
# Check if the number is greater than .51 then round the figure to higher end
# Example. num_float = 23.66 - round it to 24.

def rounding():
    user_float = float(input("Please input a float number\n -> "))
    # This checks that the remainder i.e. after decimal place is greater than .5 etc..
    if user_float % 1 < .5:
        output = math.floor(user_float)
    else:
        output = math.ceil(user_float)

    print(f"Formatted number: {output}")

rounding()
print("=" * 40)
################################################
```
### Using modules to find system information
```python
# To find out system configuration or system related information
# Based on the information provided we can handle the user request
import os, datetime, sys, math

working_dir = os.getcwd()
print(working_dir)
################################################
# Let's find out the name of our os
# print(os.uname()) THIS DOESNT WORK ON WINDOWS, ITS FOR MAC USERS
################################################
# Let's count the number of CPUs - os.cpu_count() gives total amount of CPUs in the system
print(os.cpu_count())
################################################
# datetime module gives us the ability to find the current date and time etc.
print(datetime.datetime.today())
################################################
# To find system path -----> sys.path
```
### Creating a customised method add required
information and use the functionality
provided by sys module:

```python
def current_system_path():
    print("This is your current directory:\n -> ")
    return sys.path

print(current_system_path())
```

**What is PiP?**
- Package manager for python and helps us
install external packages such as : Requests
or Emoji
- Syntax: pip install name_of_package

## APIs
![](api.PNG)
```python
# Pip install manager used to install any external packages we want to use within python
# Current package we are using is requests

# importing requests to make an api call to www
import requests
import emoji

# Provides a code for the website as a response, need to put status_code to get an integer value
live_response = requests.get("https://www.bbc.co.uk/")

print(live_response.status_code)
# print(live_response.headers)
# print(live_response.content)

# 1st Iteration - Need to write the code every time - NOT DRY
if live_response.status_code == 200:
    print(emoji.emojize("Mission Successful!! The website is live :thumbs_up:"))
elif live_response.status_code == 404:
    print(emoji.emojize("The site is unavailable until further notice... :thumbs_down:"))
else:
    print(emoji.emojize("Mission Failed.. The website is down... :thumbs_down:"))
```
### We can change the above code to improve efficiency and DRY:
```python
# 2nd Iteration - DRY desired block of code as can be used many times
def check_response_code():
    if r.status_code == 200:
        print(emoji.emojize("Website is Live! :thumbs_up:"))
    elif r.status_code == 404:
        print(emoji.emojize("Website is unavailable :sad_face:"))
    else:
        print(emoji.emojize("Website is dead... :thumbs_down:"))


def bool_response_code():
    if r.status_code == requests.codes.ok:  # => True
        print(emoji.emojize("Website is Live! :thumbs_up:"))
    elif r.status_code == requests.codes.not_found:  # => False
        print(emoji.emojize("Website is unavailable :sad_face:"))
    else:
        print(emoji.emojize("Website is dead... :thumbs_down:"))
# It will evaluate to True if the status code was between 200-400 is always a True
# otherwise False
```

### Json basics
- Java script object notation
- Use cases: browser data
- Data is in key value pairs
- Json encoding from a Dictionary
- Json decoding into a Dictionary
- Handling/creating files with python
- Writing to file
- Reading from file