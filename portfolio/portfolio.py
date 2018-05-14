# This program will be track the my portfolio
# and give me useful data such as the current
# value and percent change
# Python version 3.6.5
# Plan to add QT GUI integration eventually
import json
import requests
import os

# Take in API
baseURL = "http://coincap.io/"

def main():
    choice = '?'

# 
    options = { 1 : add,
                2 : delete,
                3 : total_val,
                4 : top_ten,
                5 : save,
                6 : load
}

    while choice != 'q':
        os.system("cls")
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
        options[choice]()


    
    
main()
