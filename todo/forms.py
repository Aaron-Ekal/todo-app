from django import forms
from django.forms import ModelForm

from todo.models import Task


from .models import *


class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = '__all__'

