# Generated by Django 3.1.7 on 2022-04-26 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_auto_20220425_2254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='component',
            name='text',
        ),
        migrations.AlterField(
            model_name='component',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='component',
            name='snum',
            field=models.CharField(max_length=400),
        ),
    ]
