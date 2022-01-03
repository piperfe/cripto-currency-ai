import requests


def make_get_ticker():
    url = 'https://www.buda.com/api/v2/markets/eth-btc/ticker'
    response = requests.get(url)
    return response
