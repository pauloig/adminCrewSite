from turtle import home
from django.contrib import admin
from django.urls import path, include
from . import views
from timesheet import views

urlpatterns = [
     path('employee_list/',views.employee_list),   
     path('create/',views.create),
     path('update/<id>',views.update),
]