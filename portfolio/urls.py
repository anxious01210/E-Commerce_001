from django.urls import path
from .views import *
app_name = 'portfolio'
urlpatterns = [
    path("work",work_view,name="work"),
    path("work-detail", work_detailes_view,name="work-detail"),
]
