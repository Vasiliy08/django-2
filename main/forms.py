from django import forms
from .models import *

class AddEmployee(forms.ModelForm):
    ruc = forms.ModelChoiceField(queryset=AllEmployees.objects.all())
    class Meta:
        model = AllEmployees
        fields = ['name', 'middle_name', 'last_name', 'INN', 'category', 'ruc']
        widgets = {

        }


