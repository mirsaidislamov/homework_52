from django import forms

from webapp.models import Tasks


class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['description', 'status', 'date_to_complete', 'detailed_description']