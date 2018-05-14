# This program will be track the my portfolio
# and give me useful data such as the current
# value and percent change
# Python version 3.6.5
# Plan to add QT GUI integration eventually
import json
import requests
import os

baseURL = "http://coincap.io/"

data = []

def add(coin, amount):
    data.append({'coin': coin, 'amount': amount})

# FUNCTIONS
def main():
    choice = '?'

    while choice != 'q':
        #os.system("cls")
        print("{:^15}".format("MENU"))
        for i in range(15): print("-", end='')
        print()
        print("1 - Add coin")
        print("2 - Delete Coin")
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
        #elif choice == 2:
        #elif choice == 3:
        #elif choice == 4:
        #elif choice == 5:
        #elif choice == 6:

        for cn in data:
          print(cn)
    
    
main()
