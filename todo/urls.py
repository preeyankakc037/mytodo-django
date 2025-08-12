# todo/urls.py
from django.urls import path
from . import views

urlpatterns = [
    
    path('add_task', views.add_task, name='add_task'), 
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),
    
]
