from django.urls import path
from .views import *

app_name= 'blog'
urlpatterns = [
    path('', blog_view, name='blog-listing'),
    path('', list_view, name='blog-grid'),
    path('', single_post_view, name='blog-single-post'),
]