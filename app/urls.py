from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('', index,name='index'),
    path('xcp/', xcp, name='xcp'),
]