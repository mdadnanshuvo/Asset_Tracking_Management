# assets/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for company detail view
    path('company/<int:company_id>/', views.company_detail, name='company_detail'),
    
    # URL pattern for adding a new company
    path('add_company/', views.add_company, name='add_company'),
    
    # URL pattern for adding a new employee
    path('add_employee/', views.add_employee, name='add_employee'),
    
    # URL pattern for assigning a device to an employee
    path('assign_device/<int:device_id>/', views.assign_device, name='assign_device'),
    
]
