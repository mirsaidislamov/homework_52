from django.shortcuts import render, get_object_or_404, redirect

from webapp.models import Tasks
from webapp.forms import TasksForm


def task_list_view(request):
    tasks = Tasks.objects.all()
    return render(request, 'task_list.html', {
        'tasks': tasks
    })


def task_create_view(request):
    if request.method == 'GET':
        form = TasksForm()
        return render(request, 'task_add.html', context={'form': form})
    elif request.method == 'POST':
        form = TasksForm(data=request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('task_detail',pk=task.id)
        else:
            return render(request, 'task_add.html', context={'form': form})

def task_update_view(request, *args, pk, **kwargs):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == 'GET':
        form = TasksForm(instance=task)
        return render(request, 'task_upgate.html', context={'form': form})
    elif request.method == 'POST':
        form = TasksForm(data=request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect('task_detail',pk=task.id)
        else:
            return render(request, 'task_upgate.html', context={'form': form})

def task_delete_view(request, *args, pk, **kwargs):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == 'GET':
        return render(request, 'task_delete.html', context={'task': task})
    elif request.method == 'POST':
        task.delete()
        tasks = Tasks.objects.all()
        return render(request,'task_list.html', context={'tasks': tasks})


def task_detail_view(request, *args, pk, **kwargs):
    task = get_object_or_404(Tasks, pk=pk)
    return render(request, 'task_detail.html', {'task': task})