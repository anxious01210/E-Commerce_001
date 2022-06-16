from django.urls import path
from .views import *
# from . import views

app_name = 'shop'
urlpatterns = [
    # path('', products, name='products'),
    path("products", product_view, name="products"),
    path("product-list", product_list_view, name="product-list"),
    path("product-detail", product_details_view, name="product-detail"),
    path("product-cart", cart_view, name="product-cart"),
    path("product-checkout", checkout_view, name="product-checkout"),

]

# urlpatterns = [
#     path("products",views.ProductView.as_view(),name="products"),
#     path("product-list",views.ProductListView.as_view(),name="product-list"),
#     path("product-detail",views.ProductDetailsView.as_view(),name="product-detail"),
#     path("product-cart",views.CartView.as_view(),name="product-cart"),
#     path("product-checkout",views.CheckoutView.as_view(),name="product-checkout"),
#
#
# ]
