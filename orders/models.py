from Crypto.Random import random
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
import uuid


# Create your models here.
from django.utils import timezone


class Coins(models.Model):
    title = models.TextField(max_length=200)
    code = models.TextField(max_length=10)

    def __str__(self):
        return self.title



def genrandom():
    num = random.randrange(0,10000)
    num2 = random.randrange(0,10000)
    prefix = "CNP"+str(num)+'-'+str(num2)
    return prefix


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    coin_amount = models.FloatField(null=False, default=0.0)
    price = models.IntegerField(null=False, default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Orders', on_delete=models.CASCADE)
    coin = models.ForeignKey(Coins, related_name='Coin', on_delete=models.CASCADE)
    order_reference = models.CharField(default=genrandom,max_length=35)
    payment_reference = models.CharField(null=True,blank=True,max_length=35)
    phone = models.IntegerField(null=True,blank=True)
    wallet = models.CharField(null=True,blank=True,max_length=100)
    date_created = models.DateTimeField(default=timezone.now)
    expired = models.BooleanField(default=False)

    PENDING = 'Pending'
    PAID = 'Paid'
    CANCELLED = 'Cancelled'
    FAILED = 'Failed'
    PROCESSING = 'Processing'
    ORDER_STATUS = [
        (PENDING, 'pending'),
        (PAID, 'paid'),
        (CANCELLED, 'cancelled'),
        (PROCESSING, 'Processing'),
        (FAILED, 'failed')]
    order_status = models.CharField(choices=ORDER_STATUS, max_length=50,default=PENDING)
    SELL = 'SELL'
    BUY = 'BUY'
    UNSPECIFIED = 'Unspecified'
    ORDER_TYPE = [
        (SELL, 'Sell'),
        (BUY, 'Buy'),
        (UNSPECIFIED,'Unspecified')]
    order_type = models.CharField(choices=ORDER_TYPE, max_length=50, default=UNSPECIFIED)

    def __str__(self):
        return str(self.id)


class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Transaction', on_delete=models.CASCADE)
    order = models.OneToOneField(Order, related_name='Orders', on_delete=models.CASCADE)
    amount = models.IntegerField()
    phone = models.IntegerField()
    PENDING = 'Pending'
    PAID = 'Paid'
    CANCELLED = 'Cancelled'
    FAILED = 'Failed'
    PROCESSING = 'Processing'
    TRANSACTION_STATUS = [
        (PENDING, 'pending'),
        (PAID, 'paid'),
        (FAILED, 'failed')]
    order_status = models.CharField(choices=TRANSACTION_STATUS, max_length=50, default=PENDING)

