from django import forms

from webapp.models import Tasks


class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['description', 'status', 'date_to_complete', 'detailed_description']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'required': 'true'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'date_to_complete': forms.DateInput(attrs={'class': 'form-control'}),
            'detailed_description': forms.Textarea(attrs={'class': 'form-control'}),
        }