import requests
from pprint import pprint

link = 'https://v6.exchangerate-api.com/v6/78a64056810980c4dec5e498/latest/USD' # List currencies

response = requests.get(link)
requested = response.json()

link_currencies = requested['conversion_rates']
currencies = []

for currency in link_currencies:
    currencies.append(currency)

for i in currencies:
    print(i)

def print_currencies(info, base):
    data = info
    currencies = info['conversion_rates']
    for currency, rate in currencies.items():
        print(f"CURRENCY: {currency} --> {rate}$")
    
    temp = base
    convert_currency(data, temp)

def convert_currency(info, base):
    requested_currency = input("CURRENCY: ").upper()
    amount = float(input("DOLLARS: "))

    currencies = info['conversion_rates']
    for currency, rate in currencies.items():
        if currency == requested_currency:
            print(f"{amount} {base} --> {round(rate * amount, 2)} {currency}")
        
def start():
    url = 'https://v6.exchangerate-api.com/v6/78a64056810980c4dec5e498/latest' # Base Currency
    base_currency = "/"

    base = input("BASE CURRENCY: ").upper()
    base_url = url + base_currency + base

    response = requests.get(base_url)
    data = response.json()

    print_currencies(data, base)

start()