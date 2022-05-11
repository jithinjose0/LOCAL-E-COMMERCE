from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
class shop_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    joindate = models.DateField(auto_now_add=True)
    email = models.EmailField(unique=True)
    #district = models.ForeignKey(District, on_delete=models.CASCADE)
    pincode = models.IntegerField()
    shop_name = models.CharField(max_length=200)
    place_name = models.CharField(max_length=100)
    licenseno = models.IntegerField()

    @staticmethod
    def get_shop_by_id(ids):
        return shop_user.objects.filter (id__in=ids)
    def __str__(self):
        return self.shop_name
   


class data(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True)
    Order_ID = models.IntegerField()
    Product = models.CharField(max_length=300, )
    Quantity = models.IntegerField()
    Price_Each = models.IntegerField()
    Order_Date = models.DateTimeField()
    Purchase_Address = models.CharField(max_length=400,)
    shop = models.CharField(max_length=200)

class ml(models.Model):
    Month = models.DateField()
    Sales = models.IntegerField()