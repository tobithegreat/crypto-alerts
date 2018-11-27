import json
import requests
from coincap_main import GLOBAL_URL, APP_KEY


def get_ticker():
    symbol = input('Please enter the symbol of the cryptocurrency: ').upper().strip()
    url = GLOBAL_URL + '/v1/cryptocurrency/quotes/latest' + '?symbol=' + symbol
    request = requests.get(url, headers = {"X-CMC_PRO_API_KEY": APP_KEY})
    results = request.json()

    data = results['data']

    currency = data[symbol]['name']
    price = data[symbol]['quote']['USD']['price']

    print('For ' + currency + ':\n\n')

    print('The current market price is: ' + str(price) + ' USD.\n')
