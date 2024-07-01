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

@login_required(login_url='/home/')
def employee_list(request):
    emp = catalogModel.Employee.objects.filter(user__username__exact = request.user.username).first()
    context ={}

    
    context["dataset"] = Timesheet.objects.filter(EmployeeID = emp, Status__in = (1,5))
    
    context["emp"]= emp

    return render(request, "timesheet/employee_list.html", context)



@login_required(login_url='/home/')
def create(request):
    emp = catalogModel.Employee.objects.filter(user__username__exact = request.user.username).first()
    context ={}

    form = TimesheetForm(request.POST or None, initial = {'EmployeeID': emp})

    if form.is_valid():
        form.instance.createdBy = request.user.username
        form.instance.created_date = datetime.now()    
        form.save()
        # Return to Locations List
        return HttpResponseRedirect('/timesheet/employee_list/')

         
    context['form']= form
    context["emp"] = emp
    return render(request, "timesheet/timesheet.html", context)


@login_required(login_url='/home/')
def update(request, id):
    emp = catalogModel.Employee.objects.filter(user__username__exact = request.user.username).first()
    context ={}

    obj = get_object_or_404(Timesheet, id = id)
    form = TimesheetForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.instance.updatedBy = request.user.username
        form.instance.updated_date = datetime.now()    
        form.save()
        # Return to Locations List
        return HttpResponseRedirect('/timesheet/employee_list/')

         
    context['form']= form
    context["emp"] = emp
    context["id"] = id
    return render(request, "timesheet/timesheet.html", context)
