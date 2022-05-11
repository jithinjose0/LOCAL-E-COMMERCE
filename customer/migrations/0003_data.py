# Generated by Django 3.1.7 on 2022-04-18 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_remove_shop_user_district'),
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('Order_ID', models.IntegerField()),
                ('Product', models.CharField(max_length=300)),
                ('Quantity', models.IntegerField()),
                ('Price_Each', models.IntegerField()),
                ('Order_Date', models.DateTimeField()),
                ('Purchase_Address', models.CharField(max_length=400)),
                ('shop', models.CharField(max_length=200)),
            ],
        ),
    ]
