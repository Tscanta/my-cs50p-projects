#Bitcoin Price Index

#To run bitcoin.py:
#1. Create a CoinCap account.
#2. Generate an API key.
#3. Replace YOUR_API_KEY in bitcoin.py with your own key.

import sys
import requests

if len(sys.argv) != 2: #the length of the command-line argument must be 2
    sys.exit("Missing command-line argument")

#converting to float
try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

API_KEY = "YOUR_API_KEY" #replace this with your API key
url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"

try:
    response = requests.get(url) #gets the JSON
    data = response.json()
    price = float(data["data"]["priceUsd"])
    amount = bitcoins * price
except requests.RequestException:
    sys.exit()

print(f"${amount:,.4f}") #prints the bitcoin price in USD with upto 4 decimal points
