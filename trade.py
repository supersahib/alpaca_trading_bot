import requests
import alpaca_trade_api as tradeapi
import sample_config as conf
import json
BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = f'{BASE_URL}/v2/account'
ORDER_URLS = f'{BASE_URL}/v2/orders'
# api = tradeapi.REST('<key_id>', '<secret_key>', api_version='v2') # or use ENV Vars shown below
# account = api.get_account()
# api.list_positions()
#https://{apiserver_domain}/v2/account

api_headers = {'APCA-API-KEY-ID': conf.API_KEY, 'APCA-API-SECRET-KEY': conf.SECRET_KEY}


def get_account():
    account_request = requests.get(ACCOUNT_URL, headers=api_headers)
    return json.loads(account_request.content)


def create_order(symbol, qty, buy_or_sell, type, time_in_force):
    order_params = {'symbol': symbol, 'qty': qty, 'side': buy_or_sell, 'type': type, 'time_in_force': time_in_force}

    create_order_request = requests.post(ORDER_URLS, headers=api_headers, json=order_params)
    return json.loads(create_order_request.content)

def get_orders(status=None, limit=None, after=None,until=None,direction=None,nested=None):
    get_order_request = requests.get(ORDER_URLS, headers=api_headers)
    return json.loads(get_order_request.content)


response = create_order('AAPL', '5', 'buy', 'market', 'day')

print(response)

response = get_orders()
print(response)