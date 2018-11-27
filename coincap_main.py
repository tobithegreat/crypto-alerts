import json
import requests
import dateutil.parser
from datetime import datetime
import coincap_ticker



GLOBAL_URL = 'https://pro-api.coinmarketcap.com'
APP_KEY = '56d9ae92-a34a-4fe7-8c85-a2fee9fd7ce8'
ticker_symbols = {}

def get_all_cryptos():
    url = GLOBAL_URL + '/v1/cryptocurrency/listings/latest'
    retrieve_results(url)

def get_market_metrics():
    url = GLOBAL_URL + '/v1/global-metrics/quotes/latest'
    results = retrieve_results(url)

    active_currencies = results['data']['active_cryptocurrencies']
    last_updated = results['data']['last_updated']
    global_cap = results['data']['quote']['USD']['total_market_cap']
    btc_percentage = results['data']['btc_dominance']
    eth_percentage = results['data']['eth_dominance']


    active_currencies_string = "{:,}".format(active_currencies)
    global_cap_string = "{:,}".format(global_cap)
    last_updated_string = dateutil.parser.parse(last_updated).strftime('%B %d, %Y at %I:%M%p, %Z time')

    print('\n\n\n')
    print('Welcome to Crypto Alerts.\n')
    print('There are currently ' + active_currencies_string + ' active currencies.\n')
    print('The current market cap is ' + global_cap_string + '.\n')
    print("Bitcoin's total percentage of the market cap is " + str(int(btc_percentage)) + "%.\n")
    print("Ethereum's total percentage of the market cap is " + str(int(eth_percentage)) + "%.\n")
    print("Information last updated at " + last_updated_string + ".\n\n")

    choice = input("Press T to access a specific cryptocurrency ticker: \n").strip().upper()

    if choice == 'T':
        coincap_ticker.get_ticker()





def retrieve_results(url):
    request = requests.get(url, headers = {"X-CMC_PRO_API_KEY": APP_KEY})
    results = request.json()
    return results

if __name__ == '__main__':
    get_market_metrics()
