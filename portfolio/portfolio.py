# This program will be track the my portfolio
# and give me useful data such as the current 
# value and percent change
# Python version 3.6.5
# Plan to add QT GUI integration eventually

import json
import requests

# Take in API
baseURL = "http://coincap.io/"
coins_api = requests.get(baseURL + "coins").text
front_api = requests.get(baseURL + "front").text

# Put into JSON
coins = json.loads(coins_api)
front = json.loads(front_api)

# Show Coins to user
for coin in front:
    print('{:<20}{:.2f}'.format(coin['long'], coin['price']))


# Ask for which coin they have

# Show their coins

# Write to file
