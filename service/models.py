from django.db import models
from numpy import empty
from django.contrib.auth.models import User
# Create your models here.
class image(models.Model):
    img = models.ImageField(upload_to='images/')
    strs = models.CharField(max_length=500)
    un = models.CharField(max_length=200)

class Comp(models.Model):
    snum = models.CharField(max_length=400)
    image = models.ImageField(upload_to='images/')
    cus_id= models.ForeignKey(User,on_delete=models.CASCADE)
    
    def text_as_list(self):
        return self.snum.split()