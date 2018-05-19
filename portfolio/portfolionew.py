# This is going to be my remake of my
# portfolio with a class this time

import json
import requests
import os

print("Loading in initial data..")

baseURL = "http://coincap.io/"
map = json.loads(requests.get(baseURL + "map").text)

class Portfolio:
  def __init__(self):
    self.data = []

  def find_ticker(self, name):
    if len(name) > 4:
      for coin in map:
        if coin.get('name', '').lower() == name.lower():
          return coin.get('symbol')
    elif len(name) <= 4:
      for coin in map:
        if coin.get('symbol', '').lower() == name.lower():
          return coin.get('symbol')

  def show(self):
    for cn in self.data:
      print(cn)

  def add(self, coin, amount):
    ticker = self.find_ticker(coin)
    if ticker != None:
      for cn in self.data:
        if cn['ticker'] == ticker:
          newamount = float(cn['amount']) + float(amount)
          cn.update({'ticker': ticker, 'amount': float(newamount)})
          return
      self.data.append({'ticker': ticker, 'amount': float(amount)})

  def remove(self, coin, amount):
    for cn in self.data:
      if cn.get('ticker', '') == self.find_ticker(coin):
        newamount = float(cn.get('amount')) - float(amount)
        if newamount < 0 : newamount = 0
        newcoin = {'ticker': self.find_ticker(coin), 'amount': newamount}
        cn.update(newcoin)

def main():
    myPF = Portfolio()

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
          myPF.add(coin, amount)
        elif choice == '2':
          coin = input("Enter the name of the coin: ")
          amount = input("Enter the amount: ")
          myPF.remove(coin, amount)


        myPF.show()

main()