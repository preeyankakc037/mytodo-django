
from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_complete=False).order_by('-updated_at')  # get only incomplete tasks
    context = {
        'tasks': tasks  # pass the queryset, not the model
    }
    return render(request, 'home.html', context)
