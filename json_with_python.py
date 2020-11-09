# Use json module to do json encoding and decoding

import json

# Creating a dictionary and storing it into a variable
car_data = {"name":"tesla", "engine":"electric"}

# json.dumps() - serialises json to a formatted string
car_data_json_string = json.dumps(car_data) # Changed dict to str

# This is how we can encode from a dictionary and write to a file
with open("new_json_file.json", "w") as jsonfile: # w is to give write permissions
    json.dump(car_data, jsonfile)

with open("new_json_file.json") as jsonfile:
    car = json.load(jsonfile) # load() copies the data and stores into a variable
    print(type(car)) # NOW ITS A DICT
    print(car['name']) # To get the name of the car in the dict
    print(car['engine']) # To get the name of the engine type of the car

# Json is used heavily in the industry, so reading(encoding),
# writing(decoding), parsing data and converting data are the
# most commonly utilised options

# Exception handling
try # if
except # elif or is it
raise # elif send back the original exception or is it
finally # else or is it

# add the exception handling required blocks to check if the file is created
# if not return back the original exception together with customised
# user friendly message