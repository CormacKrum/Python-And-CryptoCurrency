import json
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from datetime import datetime

url = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest'
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '46461c59-18e8-445d-93aa-0dfb99a9b0e0',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url)
    results = response.json()

    print(response)
    print(json.dumps(results, sort_keys=True, indent=4))

    active_currency = results["data"]["active_cryptocurrencies"]
    active_markets = results["data"]["active_market_pairs"]
    bitcoin_percentage = results["data"]["btc_dominance"]
    last_updates = results["data"]["last_updated"]
    global_cap = int(results["data"]["quote"]["USD"]["total_market_cap"])
    global_volume = int(results["data"]["quote"]["USD"]["total_volume_24h"])

    active_currency_str = '{:,}'.format(active_currency)
    active_markets_str = '{:,}'.format(active_markets)
    global_cap_str = '{:,}'.format(global_cap)
    global_volume_str = '{:,}'.format(global_volume)

    # last_updates_date = datetime.fromtimestamp(last_updates).strftime('%B %d,%Y at %I:%M%p')

    print("Active Currency :", active_currency_str)
    print("Active Market :", active_markets_str)
    print("Bitcoin Percentage :", str(bitcoin_percentage), "%")

    print("Global Capital :", global_cap_str)
    print("Global volume :", global_volume_str)

    print("The Information was last updated on :", last_updates)

except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
