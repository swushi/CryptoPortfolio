import json

data = []

def add(name, amt):
  data.append({"ticker": name, "amount": amt})

def write():
  with open('portfolio.json', 'w') as file:
    json.dump(data, file)

def load():
  with open('portfolio.json', 'r') as file:
     data = json.load(file)

def main():
  choice = input("Do you want to add vals? (y/n): ")
  if choice == 'y':    
    add('btc', 43.2)
    add('xrp', 256.5)
    add('xmr', 655.3)
    print(data)
    write()

  if choice == 'n':
    load()
    print(data)

main()
