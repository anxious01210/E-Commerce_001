from django.shortcuts import render


# Create your views here.

def product_view(request):
    context = {"title": "Product"}
    return render(request, 'shop/products.html', context)


def product_list_view(request):
    context = {"title": "Product List"}
    return render(request, 'shop/product-list.html', context)


def product_details_view(request):
    context = {"title": "Product Details"}
    return render(request, 'shop/product-detail.html', context)


def cart_view(request):
    context = {"title": "Cart "}
    return render(request, 'shop/cart.html', context)


def checkout_view(request):
    context = {"title": "Checkout"}
    return render(request, 'shop/checkout.html', context)
