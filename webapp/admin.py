from django.contrib import admin
from webapp.models import Tasks

@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'status', 'date_to_complete')
    list_filter = ('status', 'date_to_complete')
    search_fields = ('description',)

