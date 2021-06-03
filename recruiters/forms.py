from django.db.models import fields
from recruiters.models import Job
from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'salary_range', 
        'requirements', 'compulsory_school']
    