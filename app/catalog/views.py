from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth import authenticate, login as login_process
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from .models import *
from .forms import * 
from . import views
from sequences import get_next_value, Sequence

# ********************* EMPLOYEE **********************
@login_required(login_url='/home/')
def employee_list(request):
    emp = Employee.objects.filter(user__username__exact = request.user.username).first()
    context ={}

    context["dataset"] = Employee.objects.all()
    context["emp"]= emp

    return render(request, "catalog/employee_list.html", context)



@login_required(login_url='/home/')
def create_employee(request):
    emp = Employee.objects.filter(user__username__exact = request.user.username).first()

    context ={}

    form = EmployeesForm(request.POST or None)

    if form.is_valid():
        empSeq = Sequence("emp", initial_value=1500) 
        empID = str(empSeq.get_next_value())       
        form.instance.employeeID = empID
        form.instance.createdBy = request.user.username
        form.instance.created_date = datetime.now()   
        form.save()
        # Return to Emp List
        return HttpResponseRedirect('/catalog/employee_list/')
        
         
    context['form']= form
    context["emp"] = emp
    return render(request, "catalog/create_employee.html", context)

@login_required(login_url='/home/')
def update_employee(request, id):
    emp = Employee.objects.filter(user__username__exact = request.user.username).first()
    context ={}

    obj = get_object_or_404(Employee, employeeID = id)
 
    form = EmployeesForm(request.POST or None, instance = obj)
 
    if form.is_valid():
        form.instance.updatedBy = request.user.username
        form.instance.updated_date = datetime.now()    
        form.save()
        context["dataset"] = Employee.objects.all()  
        context["emp"] = emp       
        return HttpResponseRedirect('/catalog/employee_list/')

    context["form"] = form
    context["emp"] = emp
    return render(request, "catalog/create_employee.html", context)

# ********************* LOCATIONS **********************
@login_required(login_url='/home/')
def location_list(request):
    emp = Employee.objects.filter(user__username__exact = request.user.username).first()
    context ={}

    context["dataset"] = Location.objects.all()
    context["emp"]= emp

    return render(request, "catalog/location_list.html", context)


@login_required(login_url='/home/')
def create_location(request):
    emp = Employee.objects.filter(user__username__exact = request.user.username).first()

    context ={}

    form = LocationForm(request.POST or None)

    if form.is_valid():
        form.instance.createdBy = request.user.username
        form.instance.created_date = datetime.now()   
        form.save()
        # Return to Emp List
        return HttpResponseRedirect('/catalog/location_list/')
        
         
    context['form']= form
    context["emp"] = emp
    return render(request, "catalog/create_location.html", context)

@login_required(login_url='/home/')
def update_location(request, id):
    emp = Employee.objects.filter(user__username__exact = request.user.username).first()
    context ={}

    obj = get_object_or_404(Location, LocationID = id)
 
    form = LocationForm(request.POST or None, instance = obj)
 
    if form.is_valid():
        form.instance.updatedBy = request.user.username
        form.instance.updated_date = datetime.now()    
        form.save()
       
        return HttpResponseRedirect('/catalog/location_list/')

    context["form"] = form
    context["emp"] = emp
    return render(request, "catalog/create_location.html", context)