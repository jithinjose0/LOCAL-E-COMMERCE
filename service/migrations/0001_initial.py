# Generated by Django 3.1.7 on 2022-04-23 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images/')),
                ('strs', models.CharField(max_length=500)),
                ('un', models.CharField(max_length=200)),
            ],
        ),
    ]
