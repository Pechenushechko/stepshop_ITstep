from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from products.models import Product, ProductCategory

links_menu = [
    {'href': 'index', 'name': 'Home', 'route': ''},
    {'href': 'products:index', 'name': 'Products', 'route': 'products/'},
    {'href': 'about', 'name': 'About&nbsp;us', 'route': 'about/'},
    {'href': 'contacts', 'name': 'Contacts', 'route': 'contacts/'}
]


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    return []


def get_same_products(current_product):
    return Product.objects.filter(category=current_product.category).exclude(pk=current_product.pk)


def products(request, pk=None):
    title = "Products"

    products_ = Product.objects.all()
    categories_ = ProductCategory.objects.all()

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products_ = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products_ = Product.objects.filter(category__pk=pk).order_by('price')

        context = {
            'title': title,
            'links_menu': links_menu,
            'products': products_,
            'categories': categories_,
            'category': category,
            'basket': basket,
             }

        return render(request, 'products.html', context)

    context = {
        'title': title,
        'links_menu': links_menu,
        'products': products_,
        'categories': categories_,
        'basket': basket,
    }

    return render(request, 'products.html', context)


def product(request, pk):
    title = "Product"

    context = {
        'title': title,
        'links_menu': links_menu,
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
        'same_products': get_same_products(get_object_or_404(Product, pk=pk)),
    }
    return render(request, 'product.html', context)
