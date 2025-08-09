# todo/urls.py
from django.urls import path
from . import views

urlpatterns = [
    
    path('add_task', views.add_task, name='add_task'),  #  matches your form's URL
    
    
]
