from django.urls import path
from .views import *
urlpatterns = [
    path('shop_signup',shop_signup,name='shop_signup'),
    path('shop_login',shop_login,name='shop_login'),

    path('shop_home',shop_home,name='shop_home'),
    path('regproduct',regproducts,name='regproduct'),
    path('sample',sample,name='sample'),
    path('find',findingshop,name='find'),
    path('allproducts',allproducts,name='allproducts'),
    path('ordered_list',ordered_list,name='ordered_list'),


    path('homepagess',homepage,name='homepagess'),
    path('index',index,name="index"),

    path('samdash',samdash,name='samdash'),
    path('dashboard',dashboard,name='dashboard'),


    path('pro_list',pro_list,name='pro_list'),
    path('top',top,name='top'),
    path('city',city,name='city'),
    path('mls',mls,name='mls'),

    path('growth',growth,name='growth'),
    path('traffic',traffic,name='traffic'),


    path('about',about,name='about'),
    path('contact',contact,name='contact'),

    path("stat",stat,name="stat"),
    path("delete",delete,name="delete"),

    path('uploadd',uploadd,name="uploadd"),
    path('view_data',View_data,name="view_data"),
    
]
