from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *


class EmployeesListViews(ListView):
    paginate_by = 2
    model = AllEmployees
    template_name = 'main/employees_list.html'
    context_object_name = 'all_employees'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все сотрудники'
        context['count'] = len(self.model.objects.all())
        return context


class EmployeeDetailViews(DetailView):
    model = AllEmployees
    template_name = 'main/employee_detail.html'
    context_object_name = 'employee_detail'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Сотрудник {context["object"]}'
        context['card_info'] = f'{context["object"]}'
        return context


class AddEmployeeCreateViews(CreateView):
    form_class = AddEmployee
    template_name = 'main/add_employee.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Добавить сотрудника'
        return context

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        if AllEmployees.objects.filter(name=name):
            print('Создано')
            form.add_error('name', ValidationError('Уже создано'))
            return super().form_invalid(form)
        else:
            print("Не создано")
            return super().form_valid(form)


class EmployeeUpdateViews(UpdateView):
    model = AllEmployees
    form_class = AddEmployee
    template_name = 'main/update_employee.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Обновить сотрудника {context['object']}"
        return context

    # def form_valid(self, form):
    #     name = form.cleaned_data.get('name')
    #     if AllEmployees.objects.filter(name=name).exists():
    #         print('Создано')
    #         form.add_error('name', ValidationError('Уже создано'))
    #         return super().form_invalid(form)
    #     else:
    #         print("Не создано")
    #         return super().form_valid(form)


class EmployeeDeleteViews(DeleteView):
    model = AllEmployees
    template_name = 'main/delete_employee.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Удалить сотрудника {context['object']}"
        return context


class ChartsListViews(ListView):
    paginate_by = 5
    model = AllEmployees
    template_name = 'main/charts.html'
    context_object_name = 'charts'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Графики'
        context['count'] = len(self.model.objects.all())
        return context


class RegisterCreateViews(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('home')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Регистрация'
        return context