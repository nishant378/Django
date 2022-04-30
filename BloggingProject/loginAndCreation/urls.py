



#from django import views
from django.contrib import admin
from django.urls import path,include

from loginAndCreation import views

urlpatterns = [
    path('', views.index,name="index"),
    path('create', views.create,name="index"),
]





