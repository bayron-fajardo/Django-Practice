from django import forms
from .models import Task, Person

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name','description','state','fechaInicial','fechaEstimada','personas']

class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ['name','rol','yearsExperiencie','fechaIngreso','tasks']
