from turtle import home
from django.contrib import admin
from django.urls import path, include
from . import views
from catalog import views

urlpatterns = [
    #Employee
    path('employee_list/',views.employee_list),
    path('create_employee/',views.create_employee),
    path('update_employee/<id>',views.update_employee),
    #Locations
    path('location_list/',views.location_list),
    path('create_location/',views.create_location),
    path('update_location/<id>',views.update_location),

]