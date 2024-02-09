from django.contrib import admin
from django.urls import path, include
from app1.views import *
urlpatterns = [
    path('', index, name='index'), 
    path('update_server', update_server, name="update_server"),
]
