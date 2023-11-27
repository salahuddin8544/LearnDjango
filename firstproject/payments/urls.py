
from django.contrib import admin
from django.urls import path
from .views import bk, rk
urlpatterns = [
    path('bkash/',bk),
    path('rocket/',rk),
]
