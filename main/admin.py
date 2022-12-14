from django.contrib import admin
from .models import *
from . import forms


class AllEmployeesAdmin(admin.ModelAdmin):
    list_display = ['name', 'middle_name', 'last_name', 'INN', 'date_create', 'date_update', 'category', 'slug']

    form = forms.AddEmployee


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(AllEmployees, AllEmployeesAdmin)