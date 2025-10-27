from django.urls import path
from webapp.views import task_list

urlpatterns = [
    path('', task_list),
]