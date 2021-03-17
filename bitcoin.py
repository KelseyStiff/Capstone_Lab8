import requests
from pprint import pprint

def main():
    amount = get_bitcoin_amount()
    converted = convert_amount_to_bitcoin(amount)
    display_results(amount, converted)
    
def get_bitcoin_amount():
    return float(input('Enter the number of bitcoin: '))

def convert_amount_to_bitcoin(amount):
    exchange_rate = get_exchange_rate()
    converted = convert(amount, exchange_rate)
    return converted

def get_exchange_rate():
    coindesk_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(coindesk_url)
    data = response.json()
    print(data)
    dollars_exchange_rate = data['bpi']['USD']['rate_float']
    return dollars_exchange_rate

def convert(bitcoin, exchange_rate):
    bitcoin_value_in_dollars = bitcoin * exchange_rate
    return bitcoin_value_in_dollars

def display_results(bitcoin, bitcoin_value_in_dollars):
    print(f'{bitcoin} is equal to {bitcoin_value_in_dollars}')


if __name__ == '__main__':
    main()


