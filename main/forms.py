from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q
from .models import *


class AddEmployee(forms.ModelForm):
    rucod = forms.ModelChoiceField(queryset=AllEmployees.objects.filter(~Q(category=1)), to_field_name="name", required=False)
    class Meta:
        model = AllEmployees
        fields = ['name', 'middle_name', 'last_name', 'INN', 'category', 'rucod', 'calendar']
        widgets = {

        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин',widget=forms.TextInput(attrs={'class': "container",'placeholder':'qweewqweqwe'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': "container"}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': "container"}))
    email = forms.CharField(label='email', widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')

