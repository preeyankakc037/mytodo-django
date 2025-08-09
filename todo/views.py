from django.shortcuts import redirect
# from django.http import HttpResponse
from .models import Task
# Create your views here.

def add_task(request):
    if request.method == "POST":
        task = request.POST.get("task")  # This returns None if 'task' missing
        if task:  # Only create if task has a value
            Task.objects.create(task=task)
        return redirect('Home')  # Use exact name from your urls.py
    return redirect('Home')



