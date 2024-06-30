from turtle import home
from django.contrib import admin
from django.urls import path, include
from . import views
from catalog import views

urlpatterns = [
     path('employee_list/',views.employee_list),
    path('create_employee/',views.create_employee),
    path('update_employee/<id>',views.update_employee),
]