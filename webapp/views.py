from django.shortcuts import render

from webapp.models import Tasks


def task_list(request):
    tasks = Tasks.objects.all()
    context = {'tasks': tasks}
    return render(request, 'task_list.html', {'tasks': tasks})

def task_create(request):
    pass
