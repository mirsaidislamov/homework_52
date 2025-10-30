from django.urls import path
from webapp.views import task_list_view, task_create_view, task_detail_view

urlpatterns = [
    path('', task_list_view),
    path('add/', task_create_view),
    path('task/<int:pk>', task_detail_view)
]