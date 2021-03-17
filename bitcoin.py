import requests
from pprint import pprint

def main():
    amount = get_bitcoin_amount()
    converted = convert_amount_to_bitcoin(amount)
    display_results(amount, converted)
    
def get_bitcoin_amount():
    return float(input('Enter the number of bitcoin: '))

def convert_amount_to_bitcoin(amount):
    exchange_rate = get_exchange_rate(amount)
    # converted = convert(amount, exchange_rate)
    return exchange_rate

def get_exchange_rate(bitcoin):
    data = retrieve_data()
    dollars_exchange_rate = data['bpi']['USD']['rate_float']
    bitcoin_value_in_dollars = bitcoin * dollars_exchange_rate
    return bitcoin_value_in_dollars

def retrieve_data():
    coindesk_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(coindesk_url)
    data = response.json()
    return data

def display_results(bitcoin, bitcoin_value_in_dollars):
    print(f'{bitcoin} is equal to {bitcoin_value_in_dollars}')


if __name__ == '__main__':
    main()


