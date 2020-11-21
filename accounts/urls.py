from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('index',views.index,name='index'),
    path('',views.register,name='register'),
    path('shop',views.shop,name='shop'),

]