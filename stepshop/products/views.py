from django.shortcuts import render

links_menu = [
    {'href': 'index', 'name': 'Home', 'route': ''},
    {'href': 'products:index', 'name': 'Products', 'route': 'products/'},
    {'href': 'about', 'name': 'About&nbsp;us', 'route': 'about/'},
    {'href': 'contacts', 'name': 'Contacts', 'route': 'contacts/'}
]

def products(request):
    title = "Products"

    context = {
        'title': title,
        'links_menu': links_menu,
    }

    return render(request, 'products.html', context)


def product(request):
    title = "Products"

    context = {
        'title': title,
        'links_menu': links_menu,
    }
    return render(request, 'product.html', context)
