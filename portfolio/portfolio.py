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

print(type(front))
print(type(front[0]))
print(type(front[0]['price']))

# Show Coins to user
print('{:>20}     {:>10}'.format('Name', 'Price'))

for coin in front[:3]:
    print('{:>20} ==> {:>10.4f}'.format(coin['long'], coin['price']))

# Ask for which coin they have

# Show their coins

# Write to file