# Generated by Django 2.2.7 on 2019-12-01 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_order_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='expired',
            field=models.BooleanField(default=False),
        ),
    ]