# Generated by Django 3.1.7 on 2022-04-25 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_component'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='text',
            field=models.TextField(default='no text found'),
        ),
    ]
