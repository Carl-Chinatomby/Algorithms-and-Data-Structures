"""
A simple script to fetch bit coin prices in a specified currency

Supported Currencies are located here:
https://api.coindesk.com/v1/bpi/supported-currencies.json
"""


import argparse
import json
import requests


COINDESK_BASE_URL = 'https://api.coindesk.com/v1/bpi/currentprice/'
DEFAULT_CURRENCY = 'USD'


def get_current_price(currency):
    url = '{}{}.json'.format(COINDESK_BASE_URL, currency)

    resp = requests.get(url)
    try:
        current_price = json.loads(resp.content)['bpi'][currency]['rate_float']
    except (json.decoder.JSONDecodeError, KeyError):
        print("Error decoding current price. Exiting")
        exit(0)

    return current_price


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--cur', help='The currency the current price should be returned as.')
    args = parser.parse_args()
    currency = args.cur or DEFAULT_CURRENCY
    current_price = get_current_price(currency)
    print('The current price for bit coin in {} is {}'.format(currency, current_price))
