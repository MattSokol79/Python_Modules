import requests
import json

#print(live_response.status_code)

# Task
# Research how to convert this data into dictionary
# HINT - python json library/module/method can be used to resolve this
# Iterate through the data and print RESULTS
# print longitude and latitude (locations)
# Create a function that returns the longitude and latitude of the given postcode
def postcode_info():
    postcode = input("Please enter your postcode\n -> ")

    url_postcode = requests.get(f"http://api.postcodes.io/postcodes/{postcode.lower()}")
    status_of_url = url_postcode.status_code

    # .json() Turns the items into a dict that we can iterate over
    url_json = url_postcode.json()

    # If website is working, continue
    if status_of_url == requests.codes.ok:
        # For key in the sub dictionary 'result'...
        for key in url_json['result']:
            # If its postcode, provide the value for the postcode
            if key == "postcode":
                print(f"Postcode is --> {url_json['result'][key]}")
            # If its longitude, provide the value for the longitude
            elif key == 'longitude':
                print(f"Longitude is --> {url_json['result'][key]}")
            # If its latitude, provide the value for the latitude
            elif key == 'latitude':
                print(f"Latitude is --> {url_json['result'][key]}")

    else:
        print("There seems to be a problem, try again")

postcode_info()





