from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .models import Task
# Create your views here.

def add_task(request):
    if request.method == "POST":
        task = request.POST.get("task")  # This returns None if 'task' missing
        if task:  # Only create if task has a value
            Task.objects.create(task=task)
        return redirect('Home')  # Use exact name from your urls.py
    return redirect('Home')



def mark_as_done(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_complete= True
    task.save()
    return redirect('Home')

def mark_as_undone(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_complete= False
    task.save()
    return redirect('Home')


def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('Home')
    else:
        context = {
            'get_task': get_task,
        }
        return render(request, 'edit_task.html', context)


def delete_task(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('Home')