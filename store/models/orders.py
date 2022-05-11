from re import T
from djongo import models
from .product import Products
from .customer import Customer
from customer.models import shop_user
import datetime


class Order(models.Model):
    product = models.ForeignKey(Products,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                on_delete=models.CASCADE)
    #shop = models.ForeignKey(shop_user,
                                #on_delete=models.CASCADE,null=True)
    shopss = models.CharField(max_length=500,blank=True)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField (max_length=50, default='', blank=True)
    phone = models.CharField (max_length=50, default='', blank=True)
    date = models.DateField (default=datetime.datetime.today)
    status = models.BooleanField (default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

