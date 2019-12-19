import requests
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from coinbase.wallet.client import Client

from orders.models import Coins, Order


def getprice():
    client = Client(api_key='1XdFWSCd0nwzXR1C', api_secret='x0EHD2GbO3t2zmYTZJb6z0tQYh3X1MpN', api_version='2019-11-17')
    account = client.get_primary_account()
    buy_price = client.get_buy_price(currency='USD')
    sell_price = client.get_sell_price(currency='USD')
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


def HomePageView(request):
    order_list = Order.objects.all
    coins = Coins.objects.all
    rate = getbuyexchange()
    buy_price = getprice()['buy']
    buy_price = float(rate) * float(buy_price)
    sell_price = float(rate) * float(getprice()["sell"])
    context = {'order_list': order_list, 'coins': coins, 'buy_price': buy_price, 'sell_price': sell_price,}
    return render(request, 'index.html', context)
