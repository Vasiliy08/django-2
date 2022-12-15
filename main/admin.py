from django.contrib import admin
from .models import *
from . import forms


class AllEmployeesAdmin(admin.ModelAdmin):
    list_display = ['name', 'middle_name', 'last_name', 'INN', 'date_create', 'date_update', 'category', 'slug', 'dct']
    form = forms.AddEmployee


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class CalendarAdmin(admin.ModelAdmin):
    list_display = ('date_start', 'date_end', 'days')


admin.site.register(Category, CategoryAdmin)
admin.site.register(AllEmployees, AllEmployeesAdmin)
admin.site.register(Calendar, CalendarAdmin)