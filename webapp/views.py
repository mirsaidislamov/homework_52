from django.shortcuts import render
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

        if not description:
            return render(request, 'task_add.html', {
                'status_choices': STATUS_CHOICES,
                'old_description': description,
                'old_status': status,
                'old_date_to_complete': date_to_complete_str
            })

        if status not in [s[0] for s in STATUS_CHOICES]:
            status = 'new'

        date_to_complete = None
        if date_to_complete_str:
            try:
                date_to_complete = datetime.strptime(date_to_complete_str, '%Y-%m-%d').date()
            except ValueError:
                return render(request, 'task_add.html', {
                    'status_choices': STATUS_CHOICES,
                    'old_description': description,
                    'old_status': status,
                    'old_date_to_complete': date_to_complete_str
                })

        try:
            Tasks.objects.create(
                description=description,
                status=status,
                date_to_complete=date_to_complete
            )
        except Exception:
            return render(request, 'task_add.html', {
                'status_choices': STATUS_CHOICES,
                'old_description': description,
                'old_status': status,
                'old_date_to_complete': date_to_complete_str
            })

        tasks = Tasks.objects.all()
        return render(request, 'task_add.html', {
            'tasks': tasks,
            'success': 'Задача успешно добавлена!'
        })

