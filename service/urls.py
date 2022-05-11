from django.urls import path
from .views import *
urlpatterns = [

    path('service_signup',service_signup,name='service_signup'),
    path('service_login',service_login,name='service_login'),
    path('service_home',service_home,name='service_home'),
    path('logout',logout_view,name='logout'),

    path('upload_img',upload_page,name='upload_img'),
    path('scan_view',scan_view,name='scan_view'),
    path('sales_data',sales,name='sales_data'),

    path('profile_view',profile_view,name="profile_view"),

]