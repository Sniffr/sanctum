# Generated by Django 2.2.7 on 2019-12-05 09:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0014_auto_20191204_1329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('order_status', models.CharField(choices=[('Pending', 'pending'), ('Paid', 'paid'), ('Failed', 'failed')], default='Pending', max_length=50)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Orders', to='orders.Order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
