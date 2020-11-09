# Pip install manager used to install any external packages we want to use within python
# Current package we are using is requests

# importing requests to make an api call to www
import requests
import emoji

# Provides a code for the website as a response, need to put status_code to get an integer value
live_response = requests.get("https://www.bbc.co.uk/")

print(live_response.status_code)

if live_response.status_code == 200:
    print(emoji.emojize("Mission Successful!! The website is live :thumbs_up:"))
else:
    print(emoji.emojize("Mission Failed.. The website is down... :thumbs_down:"))

