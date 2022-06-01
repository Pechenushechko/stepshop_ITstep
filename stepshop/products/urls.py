from django.urls import path

from products.views import products, product

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('product/', product),
]
