from django.shortcuts import render


links_menu = [
    {'href': 'index', 'name': 'Home', 'route': ''},
    {'href': 'products:index', 'name': 'Products', 'route': 'products/'},
    {'href': 'about', 'name': 'About&nbsp;us', 'route': 'about/'},
    {'href': 'contacts', 'name': 'Contacts', 'route': 'contact/'}
]


def index(request):
    title = "main page"

    context = {
        'title': title,
        'links_menu': links_menu,
    }

    return render(request, "index.html", context)


def about(request):
    title = "About us"

    context = {
        'title': title,
        'links_menu': links_menu,
    }
    return render(request, "about.html", context)


def contact(request):
    title = "Contacts"

    context = {
        'title': title,
        'links_menu': links_menu,
    }
    return render(request, "contact.html", context)


