from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect, response, HttpResponse, HttpResponseServerError
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic
import json
from modules_scripts.modules import *
from modules_scripts.wallets_CB import *

from .models import Order, Coins, Transaction

CB = CoinBase()


def sell_coin_price(coin_amount, coin):
    if coin == "btc":
        rate = getbuyexchange()
        price = getprice()
        amount = float(coin_amount) * float(price["sell"])
        amount = amount * 0.9
        return amount * rate
    if coin == "ltc":
        rate = getbuyexchange()
        price = get_ltc_price()
        amount = float(coin_amount) * float(price["sell"])
        amount = amount * 0.9
        return amount * rate
    if coin == "eth":
        rate = getbuyexchange()
        price = get_eth_price()
        amount = float(coin_amount) * float(price["sell"])
        amount = amount * 0.9
        return amount * rate


def buy_coin_price(coin_amount, coin):
    if coin == "btc":
        rate = getbuyexchange()
        price = getprice()
        amount = float(coin_amount) * float(price["buy"])
        amount = amount * 1.1
        return amount * rate
    if coin == "ltc":
        rate = getbuyexchange()
        price = get_ltc_price()
        amount = float(coin_amount) * float(price["buy"])
        amount = amount * 1.1
        return amount * rate
    if coin == "eth":
        rate = getbuyexchange()
        price = get_eth_price()
        amount = float(coin_amount) * float(price["buy"])
        amount = amount * 1.1
        return amount * rate


# Create your views here.


def OrderView(request):
    try:
        order_list = Order.objects.all().filter(user_id=request.user.id, expired=False, )
        print(order_list.count())
        for order in order_list:
            showablelist = [order.FAILED, order.PAID, order.PROCESSING]
            if ((order.order_status not in showablelist) and (
                    timezone.now() - order.date_created).total_seconds() > 1800):
                order.expired = True
                order.save()
        order_list = order_list.exclude(expired=True)
        print(order_list.count())
        coins = Coins.objects.all()
        context = {'order_list': order_list, 'coins': coins}
        return render(request, 'orders.html', context)
    except Exception as e:
        print(e)
        print(traceback.format_exc())

        raise HttpResponseServerError()


def Buyorder(request):
    rate = getbuyexchange()
    sellrate = getsellexchange()
    buy_price = getprice()['buy']
    buy_price = float(rate) * float(buy_price)
    sell_price = float(rate) * float(getprice()["sell"])
    context = {'buy_price': buy_price, 'sell_price': sell_price}
    return render(request, 'buy.html', context)


def Buy_ltc_order(request):
    rate = getbuyexchange()
    sellrate = getsellexchange()
    buy_price = get_ltc_price()['buy']
    buy_price = float(rate) * float(buy_price)
    sell_price = float(sellrate) * float(get_ltc_price()["sell"])
    context = {'buy_price': buy_price, 'sell_price': sell_price}
    return render(request, 'buy_ltc.html', context)


def Buy_eth_order(request):
    rate = getbuyexchange()
    sellrate = getsellexchange()
    buy_price = get_eth_price()['buy']
    buy_price = float(rate) * float(buy_price)
    sell_price = float(rate) * float(get_eth_price()["sell"])
    context = {'buy_price': buy_price, 'sell_price': sell_price}
    return render(request, 'buy_eth.html', context)


def Sellorder(request):
    rate = getbuyexchange()
    sellrate = getsellexchange()
    buy_price = getprice()['buy']
    buy_price = float(rate) * float(buy_price)
    sell_price = float(rate) * float(getprice()["sell"])
    context = {'buy_price': buy_price, 'sell_price': sell_price}
    return render(request, 'sell.html', context)


def Sell_eth_order(request):
    rate = getbuyexchange()
    sellrate = getsellexchange()
    buy_price = get_eth_price()['buy']
    buy_price = float(rate) * float(buy_price)
    sell_price = float(rate) * float(get_eth_price()["sell"])
    context = {'buy_price': buy_price, 'sell_price': sell_price}
    return render(request, 'sell_eth.html', context)


def Sell_ltc_order(request):
    rate = getbuyexchange()
    sellrate = getsellexchange()
    buy_price = get_ltc_price()['buy']
    buy_price = float(rate) * float(buy_price)
    sell_price = float(rate) * float(get_ltc_price()["sell"])
    context = {'buy_price': buy_price, 'sell_price': sell_price}
    return render(request, 'sell_eth.html', context)


def CreateOrder(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            try:
                if request.POST['order_type'] == "buy":
                    selected_coin = request.POST['coin_type']
                    coin = Coins.objects.get(code__contains=selected_coin)
                    user = get_user_model().objects.get(id=request.user.id)
                    if request.POST['coin_amount']:
                        coin_amount = float(request.POST['coin_amount'])
                        amount = int(buy_coin_price(coin_amount, selected_coin))
                    if request.POST['order_type']:
                        type = request.POST['order_type']
                    order = Order.objects.create(coin_amount=coin_amount, user=user, coin=coin, price=amount)
                    return HttpResponseRedirect(reverse('orders:Order_Details', kwargs={'pk': order.id}))

                elif request.POST['order_type'] == "sell":
                    selected_coin = request.POST['coin_type']
                    coin = Coins.objects.get(code__contains=selected_coin)
                    user = get_user_model().objects.get(id=request.user.id)
                    if request.POST['coin-amount-sell']:
                        coin_amount = float(request.POST['coin-amount-sell'])
                        amount = int(sell_coin_price(coin_amount, selected_coin))
                    if request.POST['order_type']:
                        type = request.POST['order_type']
                    order = Order.objects.create(coin_amount=coin_amount, user=user, coin=coin, price=amount)
                    return HttpResponseRedirect(reverse('orders:Order_Sell_Details', kwargs={'pk': order.id}))

            except Exception as e:
                print(e)
                print(traceback.format_exc())
                raise HttpResponseServerError()
        else:
            rate = getbuyexchange()
            sellrate = getsellexchange()
            buy_price = getprice()['buy']
            buy_price = float(rate) * float(buy_price)
            sell_price = float(sellrate) * float(buy_price)
            context = {'buy_price': buy_price, 'sell_price': sell_price}
            return render(request, 'buy.html', context)
    else:
        if request.method == "POST":
            try:
                if request.POST['order_type'] == "buy":
                    if request.POST['coin_amount']:
                        coin_amount = float(request.POST['coin_amount'])
                    if request.POST['price']:
                        price = int(request.POST['price'])
                    if request.POST['order_type']:
                        type = request.POST['order_type']
                    return redirect('account_login')
                elif request.POST['order_type'] == "sell":
                    if request.POST['coin-amount-sell']:
                        coin_amount_sell = float(request.POST['coin-amount-sell'])
                    if request.POST['price-to-sell']:
                        price_to_sell = int(request.POST['price-to-sell'])
                    if request.POST['order_type']:
                        type = request.POST['order_type']
                    return redirect('account_login')
            except Exception as e:
                print(e)
                print(traceback.format_exc())

                raise HttpResponseServerError()
        else:
            return redirect('account_login')


class DisplayBuyOrder(generic.DetailView):
    model = Order
    template_name = 'orderdetails.html'
    context_object_name = 'order_details'


def DisplaySellOrder(request, pk):
    try:
        if request.method == "POST":
            order = Order.objects.get(id=pk)

            order.phone = request.POST['phone']
            coin = order.coin.code.lower()
            print(coin)
            if len(order.wallet) < 1:
                if coin == "btc":
                    wallet = CB.create_address(CB.btc_id)
                    order.wallet = wallet
                    print("btc wallet created ")
                    order.save()
                elif coin == "ltc":
                    wallet = CB.create_address(CB.ltc_id)
                    order.wallet = wallet
                    order.save()

                elif coin == "eth":
                    wallet = CB.create_address(CB.eth_id)
                    order.wallet = wallet
                    order.save()

            print(order.wallet)
            order.save()
            context = {'order_details': order}
            return render(request, 'sellorderdetails.html', context)
        else:
            order = Order.objects.get(id=pk)
            print(order.wallet)
            context = {'order_details': order}
            return render(request, 'sellorderdetails.html', context)
    except Exception as e:
        print(traceback.format_exc())
        raise HttpResponseServerError()


def OrderSuccess(request, order_id, hash):
    try:
        if check_id(hash, order_id) == True:
            order = Order.objects.get(id=order_id)
            order.order_status = order.PAID
            wallet = order.wallet
            coin = order.coin.code.upper()
            coin_amount = order.coin_amount
            if coin == "BTC":
                CB.send_coin(wallet, coin, coin_amount, CB.btc_id)
            elif coin == "LTC":
                CB.send_coin(wallet, coin, coin_amount, CB.ltc_id)
            elif coin == "ETH":
                CB.send_coin(wallet, coin, coin_amount, CB.eth_id)
            # send confirmation mail
            order.save()
            context = {'order_reference': order.order_reference, "amount": order.coin_amount, "price": order.price}
            return render(request, context=context, template_name='success.html')
    except Exception as e:
        print(e)
        print(traceback.format_exc())

        raise HttpResponseServerError()


def OrderFailed(request, order_id, hash):
    try:
        if check_id(hash, order_id) == True:
            order = Order.objects.get(id=order_id)
            order.order_status = order.FAILED
            order.save()
            return render(request, 'Failed.html')
    except Exception as e:
        print(traceback.format_exc())
        raise HttpResponseServerError()


@csrf_exempt
def processOrderStatus(request):
    # updates transaction number and status
    data = json.loads(request.body)
    print(data)
    order = Order.objects.get(phone=data['account'])
    order.order_status = order.PAID
    id = request.user.id
    return redirect('orders:Orders', user_id=id)


@csrf_exempt
def processSellOrder(request):
    # updates transaction number and status
    data = json.loads(request.body)
    print(data)
    order = Order.objects.get(phone=data['account'])
    order.order_status = order.PAID
    #run spektra pay api
    return redirect('orders:Orders', user_id=id)


def processOrder(request):
    def spektraCheckoutLink(amount, reference, transaction_id, order_id):
        hash = gen_checkout_id(order_id)
        url = "https://api.spektra.co/api/v1/checkout/initiate"
        link_pass = request.build_absolute_uri(
            reverse('orders:success', kwargs={'order_id': str(order_id), 'hash': hash}))
        print(link_pass)
        link_fail = request.build_absolute_uri(
            reverse('orders:failed', kwargs={'order_id': str(order_id), 'hash': hash}))

        # request payload
        # spektraAccountName is Optional, used for subaccount-specific payments
        payload = {
            "amount": amount,
            "cancelURL": str(link_fail),
            "currency": "KES",
            "description": reference,
            "successURL": str(link_pass)
        }
        # pass authorization token obtained during authentication in headers
        authcode = str(auth())
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + authcode
        }
        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
        # Print response data
        print(response.json())
        data = response.json()
        return 'https://checkout.spektra.co/' + data['checkoutID']

    if request.method == "POST":
        global order_id
        try:
            order_id = request.POST['order_id']
        except Exception  as e:
            print(e)
            print(traceback.format_exc())

            raise HttpResponseServerError()
        order = Order.objects.get(id=order_id)
        try:
            wallet = request.POST['wallet']
            order.wallet = wallet
        except Exception  as e:
            print(e)
            print(traceback.format_exc())

            raise HttpResponseServerError()
        try:
            phone = request.POST['phone']
            order.phone = phone
        except Exception as e:
            print(e)
            print(traceback.format_exc())

            raise HttpResponseServerError()
        order.save()
    try:
        current_user = get_user_model().objects.get(id=request.user.id)
        Transaction.objects.get_or_create(user=current_user, order=order, amount=order.price, phone=order.phone)
        trans = Transaction.objects.get(order=order)
        link = spektraCheckoutLink(order.price, order.order_reference, trans.id, order.id)
        return redirect(link)
    except Exception as e:
        print(e)
        print(traceback.format_exc())

        # redirect to 404
        raise HttpResponseServerError()
