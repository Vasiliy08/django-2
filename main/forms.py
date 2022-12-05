from django import forms
from .models import *

class AddEmployee(forms.ModelForm):
    class Meta:
        model = AllEmployees
        fields = ['name', 'middle_name', 'last_name', 'INN', 'category']
