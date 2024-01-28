# assets/models.py
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        app_label = 'assets'
    

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    

class Device(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Employee, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=100)
    checked_out_time = models.DateTimeField(blank=True, null=True)
    checked_in_time = models.DateTimeField(blank=True, null=True)
    
