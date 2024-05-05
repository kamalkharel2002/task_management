from django import forms
from django.forms import fields
from taskapp.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'duedate']
