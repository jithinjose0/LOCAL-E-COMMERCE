# Generated by Django 3.1.7 on 2022-04-18 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_order_shop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='fkk',
        ),
    ]
