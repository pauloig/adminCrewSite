from turtle import home
from django.contrib import admin
from django.urls import path, include
from . import views
from timesheet import views

urlpatterns = [
     path('employee_list/',views.employee_list),   
     path('create/',views.create),
     path('update/<id>',views.update),
     path('create/',views.create),
     # ****** Supervisor **********************
     path('supervisor_list/',views.supervisor_list), 
     path('create_by_supervisor/',views.createBySupervisor),
     path('update_by_super/<id>',views.updateBySuper),
     path('update_status/<id>/<status>',views.update_status),
     
]