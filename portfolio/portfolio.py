# This program will be track the my portfolio
# and give me useful data such as the current
# value and percent change
# Python version 3.6.5
# Plan to add QT GUI integration eventually
import json
import requests
import os

print("Loading in initial data..")

baseURL = "http://coincap.io/"
map = json.loads(requests.get(baseURL + "map").text)

data = []

# This function will find the 3 letter code
# given to a currency with any input

# FUNCTIONS
def find_ticker(name):
  if len(name) > 4:
    for coin in map:
      if coin.get('name', '').lower() == name.lower():
        return coin.get('symbol')
  elif len(name) <= 4:
    for coin in map:
      if coin.get('symbol', '').lower() == name.lower():
        return coin.get('symbol')
            

def add(coin, amount):
  ticker = find_ticker(coin)
  if ticker != None:
    for cn in data:
      if cn['ticker'] == ticker:
        newamount = float(cn['amount']) + float(amount)
        cn.update({'ticker': ticker, 'amount': float(newamount)})
        return
    data.append({'ticker': ticker, 'amount': float(amount)})

def remove(coin, amount):
  for cn in data:
      if cn.get('ticker', '') == find_ticker(coin):
          newamount = float(cn.get('amount')) - float(amount)
          if newamount < 0 : newamount = 0
          newcoin = {'ticker': find_ticker(coin), 'amount': newamount}
          cn.update(newcoin)
    
def main():
    choice = '?'

    while choice != 'q':
        #os.system("cls")
        print("{:^15}".format("MENU"))
        for i in range(15): print("-", end='')
        print()
        print("1 - Add coin")
        print("2 - Remove Coin")
        print("3 - Portfolio Value")
        print("4 - List top 10 coins, their value and volume")
        print("5 - Save data")
        print("6 - Load data")
        print("q - Quit")
        print()
        choice = input("Enter in a command: ")

        if choice == '1':
          coin = input("Enter the name of the coin: ")
          amount = input("Enter the amount: ")
          add(coin, amount)
        elif choice == '2':
          coin = input("Enter the name of the coin: ")
          amount = input("Enter the amount: ")
          remove(coin, amount)
        #elif choice == 3:
        #elif choice == 4:
        #elif choice == 5:
        #elif choice == 6:

        for cn in data:
          print(cn)
    
    
main()
