from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('about.html',views.about, name="about"),
    path('skating.html',views.skating, name="skating"),
    path('shop.html',views.shop, name="shop"),
    path('contact.html',views.contact, name="contact"),
]