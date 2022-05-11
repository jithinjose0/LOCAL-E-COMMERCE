from djongo import models
from .category import Category
from django.contrib.auth.models import User
from customer.models import shop_user
class Products(models.Model):
    name = models.CharField(max_length=60)
    price= models.IntegerField(blank=True, null=True)
    category= models.ForeignKey(Category,on_delete=models.CASCADE,default=1 )
    shops = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    description= models.CharField(max_length=250)
    image= models.ImageField(upload_to='uploads/products/')
    #, default='', blank=True, null= True
    def __str__(self):
        return self.name

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter (id__in=ids)
    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter (category=category_id)
        else:
            return Products.get_all_products();
    
