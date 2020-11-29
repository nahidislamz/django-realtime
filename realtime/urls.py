
from django.contrib import admin
from django.urls import path
from product.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', productView),
    path('product', getProduct, name="product"),
]
