from django.contrib import admin
from django.urls import path,include 
from django.conf import settings 
from django.conf.urls.static import static 
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('reirter',views.register,name='register'),
    path('shop',views.shop,name='shop'),
    path('success', views.success, name = 'success'),
    path('images', views.display_images, name = 'images'),
    path('logout', views.logout, name = 'logout')

]
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)