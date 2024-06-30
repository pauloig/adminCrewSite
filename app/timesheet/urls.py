from turtle import home
from django.contrib import admin
from django.urls import path, include
from . import views
from timesheet import views

urlpatterns = [
     path('employee_list/',views.employee_list),   
]