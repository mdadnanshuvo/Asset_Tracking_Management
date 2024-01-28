# assets/forms.py
from django import forms
from .models import Company, Employee
from .models import Device
from django.shortcuts import render, redirect, get_object_or_404




class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name'] 

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['company', 'name', 'email']  

class DeviceAssignmentForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['assigned_to', 'checked_out_time']  

class DeviceAssignmentForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['assigned_to', 'checked_out_time']

    def clean_checked_out_time(self):
        checked_out_time = self.cleaned_data.get('checked_out_time')
        if checked_out_time is not None and checked_out_time.date() < datetime.date.today():
            raise forms.ValidationError("Checked out date cannot be in the past.")
        return checked_out_time