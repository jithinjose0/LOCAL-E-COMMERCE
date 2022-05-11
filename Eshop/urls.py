from django.contrib import admin
from django.urls import path  , include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('store.urls')),
    path('cus/' , include('customer.urls')),
    path('ser/' , include('service.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
