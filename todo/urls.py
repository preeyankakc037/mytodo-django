# todo/urls.py
from django.urls import path
from . import views

urlpatterns = [

    # Add Task 
    path('add_task', views.add_task, name='add_task'), 

    # Mark as Done
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),

    # Mark as Undone 
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),
    
    # Edit Features 
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),

    # Delete Task 
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),

]
