from django.contrib import admin


# Register your models here.

from .models import Order,Coins



admin.site.register(Order)
admin.site.register(Coins)