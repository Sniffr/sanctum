# Generated by Django 2.2.7 on 2019-11-29 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20191129_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='wallet',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]