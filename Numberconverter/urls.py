from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


from Base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', views.register, name='register'),
   
    ]