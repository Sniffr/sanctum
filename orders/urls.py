from django.contrib import admin
from django.urls import include, path
from orders import views

app_name = 'orders'
urlpatterns = [
    path('dashboard', views.OrderView, name='Orders'),
    path('create/', views.CreateOrder, name='Create_Order'),
    path('details/buy/?=<uuid:pk>', views.DisplayBuyOrder.as_view(), name='Order_Details'),
    path('details/sell/?=<uuid:pk>', views.DisplaySellOrder, name='Order_Sell_Details'),
    path('checkout/', views.processOrder, name='Checkout'),
    path('status', views.processOrderStatus, name='OrderStatus'),
    path('status/sell', views.processSellOrder, name='SellOrder'),
    path('buy/', views.Buyorder, name='buy_order'),
    path('buy/eth', views.Buy_eth_order, name='buy_eth_order'),
    path('buy/ltc', views.Buy_ltc_order, name='buy_ltc_order'),
    path('sell/', views.Sellorder, name='sell_order'),
    path('sell/eth', views.Sell_eth_order, name='sell_eth_order'),
    path('sell/ltc', views.Sell_ltc_order, name='sell_ltc_order'),
    path('?=+mnb<uuid:order_id>/success/<hash>', views.OrderSuccess, name='success'),
    path('?=spl<uuid:order_id>/failed/<hash>', views.OrderFailed, name='failed'),
]
