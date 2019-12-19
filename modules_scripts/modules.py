import requests
from coinbase.wallet.client import Client
import uuid
import hashlib


def getprice():
    client = Client(api_key='1XdFWSCd0nwzXR1C', api_secret='x0EHD2GbO3t2zmYTZJb6z0tQYh3X1MpN', api_version='2019-11-17')
    account = client.get_primary_account()
    buy_price = client.get_buy_price(currency='USD')
    sell_price = client.get_sell_price(currency='USD')
    prices = {"buy": buy_price["amount"], "sell": sell_price["amount"]}
    return prices


def get_ltc_price():
    client = Client(api_key='1XdFWSCd0nwzXR1C', api_secret='x0EHD2GbO3t2zmYTZJb6z0tQYh3X1MpN', api_version='2019-11-17')
    account = client.get_primary_account()
    buy_price = client.get_buy_price(currency_pair="LTC-USD")
    sell_price = client.get_sell_price(currency_pair="LTC-USD")
    prices = {"buy": buy_price["amount"], "sell": sell_price["amount"]}
    return prices


def get_eth_price():
    client = Client(api_key='1XdFWSCd0nwzXR1C', api_secret='x0EHD2GbO3t2zmYTZJb6z0tQYh3X1MpN', api_version='2019-11-17')
    account = client.get_primary_account()
    buy_price = client.get_buy_price(currency_pair="ETH-USD")
    sell_price = client.get_sell_price(currency_pair="ETH-USD")
    prices = {"buy": buy_price["amount"], "sell": sell_price["amount"]}
    return prices


# def getbuyexchange():
#     url = "https://free.currconv.com/api/v7/convert?q=USD_KES&apiKey=759ee01132696f2ea5f6"
#     # pass authorization token obtained during authentication in headers
#     headers = {
#         'Content-Type': "application/json",
#     }
#     response = requests.request("GET", url, headers=headers)
#     # Print response data
#     data = response.json()
#     return data['results']['USD_KES']['val']


def getbuyexchange():
    url = "https://openexchangerates.org/api/latest.json?app_id=22246865dbbb47ac9f99b967d7a42ef7&symbols=KES"
    # pass authorization token obtained during authentication in headers
    headers = {
        'Content-Type': "application/json",
    }
    response = requests.request("GET", url, headers=headers)
    # Print response data
    data = response.json()
    return data['rates']['KES']


def getsellexchange():
    url = "https://free.currconv.com/api/v7/convert?q=KES_USD&apiKey=759ee01132696f2ea5f6"
    # pass authorization token obtained during authentication in headers
    headers = {
        'Content-Type': "application/json",
    }
    response = requests.request("GET", url, headers=headers)
    # Print response data
    data = response.json()
    return data['results']['KES_USD']['val']


def auth():
    url = "https://api.spektra.co/oauth/token?grant_type=client_credentials"
    # pass authorization token obtained during authentication in headers
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Basic NGY0N2E1Y2IyM2NlNDYwYWJlZmJkYTFlZDQ4MDBmN2E6NWYwZTA5ODBhZWY1NDdiYTlhOTQwNGZlYjRiYjg3MjFiMzg1MTI3ZjY1Yjk0MDA5YjIwZTA1ZTkxODg5MjYzZA=="
    }
    response = requests.request("POST", url, headers=headers)
    # Print response data
    data = response.json()

    return data["access_token"]


def test_auth():
    url = "https://api-test.spektra.co/oauth/token?grant_type=client_credentials"
    # pass authorization token obtained during authentication in headers
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Basic ZWExOGY5ODI2ZjAxNDZlYWIzZGRlZjYwNGY0NzEzODM6OGEwMWM0MDhlMjI2NDBhYmFkNWE2OGYzYTVjYzYwMjEzNGUzOTRmNTZkOGU0NDQ2YTQ5OTZhOWMzYWJiOTcyZg=="
    }
    response = requests.request("POST", url, headers=headers)
    # Print response data
    data = response.json()

    return data["access_token"]


def gen_checkout_id(order_id):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + order_id.hex.encode()).hexdigest() + '?=' + salt


def check_id(hashed_password, order_id):
    password, salt = hashed_password.split('?=')
    return password == hashlib.sha256(salt.encode() + order_id.hex.encode()).hexdigest()
