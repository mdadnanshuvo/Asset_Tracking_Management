
# assets/views.py

from .models import Company, Employee, Device
from .forms import CompanyForm, EmployeeForm
from .models import Device
from django.shortcuts import render, redirect, get_object_or_404
from .forms import DeviceAssignmentForm


def company_detail(request, company_id):
    company = Company.objects.get(id=company_id)
    employees = Employee.objects.filter(company=company)
    devices = Device.objects.filter(company=company)
    return render(request, 'company_detail.html', {'company': company, 'employees': employees, 'devices': devices})

def add_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company_list')  # Redirect to company list page
    else:
        form = CompanyForm()
    return render(request, 'add_company.html', {'form': form})

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list') 
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})

def assign_device(request, device_id):
    device = Device.objects.get(id=device_id)
    if request.method == 'POST':
        form = DeviceAssignmentForm(request.POST, instance=device)
        if form.is_valid():
            form.save()
            return redirect('device_list')  
    else:
        form = DeviceAssignmentForm(instance=device)
    return render(request, 'assign_device.html', {'form': form, 'device': device})

def assign_device(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    if request.method == 'POST':
        form = DeviceAssignmentForm(request.POST, instance=device)
        if form.is_valid():
            # Ensure the device is available
            if device.assigned_to is None:
                form.save()
                return redirect('device_list')  # Redirect to device list page
            else:
                # Device is already assigned
                return render(request, 'device_not_available.html', {'device': device})
    else:
        form = DeviceAssignmentForm(instance=device)
    return render(request, 'assign_device.html', {'form': form, 'device': device})