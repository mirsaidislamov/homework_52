from django.shortcuts import render, get_object_or_404, redirect
from .models import Tasks, STATUS_CHOICES
from datetime import datetime


def task_list_view(request):
    tasks = Tasks.objects.all()
    return render(request, 'task_list.html', {
        'tasks': tasks
    })


def task_create_view(request):
    if request.method == 'GET':
        return render(request, 'task_add.html', {
            'status_choices': STATUS_CHOICES
        })
    elif request.method == 'POST':
        description = request.POST.get('description')
        status = request.POST.get('status')
        date_to_complete_str = request.POST.get('date_to_complete')
        detailed_description = request.POST.get('detailed_description')

        if not description:
            return render(request, 'task_add.html')

        if status not in [s[0] for s in STATUS_CHOICES]:
            status = 'new'

        date_to_complete = None
        if date_to_complete_str:
            try:
                date_to_complete = datetime.strptime(date_to_complete_str, '%Y-%m-%d').date()
            except ValueError:
                return render(request, 'task_add.html')

        try:
            task = Tasks.objects.create(
                description=description,
                status=status,
                date_to_complete=date_to_complete,
                detailed_description = detailed_description
            )
            return redirect('task_detail', pk=task.pk)
        except Exception:
            return redirect('task_create')


def task_detail_view(request, *args, pk, **kwargs):
    task =get_object_or_404(Tasks, pk=pk)
    return render(request, 'task_detail.html', {'task': task})