from contextlib import nullcontext
from operator import truediv
from pyexpat import model
from random import choices
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime

class Location(models.Model):
    LocationID = models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(null=True, blank=True)
    createdBy = models.CharField(max_length=60, blank=True, null=True)
    updated_date = models.DateTimeField(null=True, blank=True)
    updatedBy = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    employeeID = models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_initial = models.CharField(max_length=100, blank=True, null= True)
    termination_date = models.CharField(max_length=200, blank=True, null= True)
    hire_created =  models.CharField(max_length=200, blank=True, null= True)
    hourly_rate = models.CharField(max_length=200, blank=True, null= True)
    email = models.CharField(max_length=200, blank=True, null= True)
    Location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL, db_column='user')
    is_active = models.BooleanField(default=True)
    is_supervisor = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created_date = models.DateTimeField(null=True, blank=True)
    createdBy = models.CharField(max_length=60, blank=True, null=True)
    updated_date = models.DateTimeField(null=True, blank=True)
    updatedBy = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.first_name + ", " + self.last_name