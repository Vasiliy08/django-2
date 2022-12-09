from django.urls import path
from .views import *


urlpatterns = [
    path('', EmployeesListViews.as_view(), name='home'),
    path('employee_detail/<slug:slug>/', EmployeeDetailViews.as_view(), name='employee_detail'),
    path('add_employee/', AddEmployeeCreateViews.as_view(), name='add_employee'),
    path('update_employee/<slug:slug>/', EmployeeUpdateViews.as_view(), name='update_employee'),
    path('delete_employee/<slug:slug>/', EmployeeDeleteViews.as_view(), name='delete_employee'),
    path('charts/', ChartsListViews.as_view(), name='charts')

]