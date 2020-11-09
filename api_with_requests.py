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

######################################################
