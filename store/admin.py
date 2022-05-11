from django.contrib import admin
from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from django_summernote.models import Attachment

admin.site.unregister(Attachment)

#class AdminProduct(admin.ModelAdmin):
    #list_display = ['name', 'price', 'category'],AdminProduct
from django.contrib.auth.models import Group

admin.site.unregister(Group)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
admin.site.register(Products)
#admin.site.register(Category)
admin.site.register(Customer)
#admin.site.register(Order)

admin.site.site_header = 'L-E-COMMERCE'
admin.site.site_title = 'L-E-COMMERCE'
admin.site.site_url = 'http://127.0.0.1:8000/cus/homepagess'
admin.site.index_title = 'Admin'
admin.empty_value_display = '**Empty**'



from django.contrib.admin.models import LogEntry

LogEntry.objects.all().delete()


from customer.models import shop_user,District
# Register your models here.
admin.site.register(shop_user)
#admin.site.register(District)
