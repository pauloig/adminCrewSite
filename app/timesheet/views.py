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
def employee_submitted_list(request):
    emp = catalogModel.Employee.objects.filter(user__username__exact = request.user.username).first()
    context ={}

    
    context["dataset"] = Timesheet.objects.filter(EmployeeID = emp, Status__in = (2,3,4))
    
    context["emp"]= emp

    return render(request, "timesheet/employee_submitted_list.html", context)



@login_required(login_url='/home/')
def create(request):
    emp = catalogModel.Employee.objects.filter(user__username__exact = request.user.username).first()
    context ={}

    form = TimesheetForm(request.POST or None, initial = {'EmployeeID': emp})

    if form.is_valid():
        form.instance.createdBy = request.user.username
        form.instance.created_date = datetime.now()    
        form.instance.total_mileage = form.instance.end_mileage - form.instance.start_mileage
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

    if int(obj.Status) >= 2 and int(obj.Status) <= 4:
        form = TimesheetDisabledForm(request.POST or None, instance = obj)
    else: 
        form = TimesheetForm(request.POST or None, instance = obj)

    if form.is_valid():
        if request.POST.get('newstatus') != '' :
            form.instance.Status = request.POST.get('newstatus')

        form.instance.total_mileage = form.instance.end_mileage - form.instance.start_mileage
        form.instance.updatedBy = request.user.username
        form.instance.updated_date = datetime.now()    
        form.save()
        # Return to Locations List
        return HttpResponseRedirect('/timesheet/employee_list/')

    context["object"] = obj     
    context['form']= form
    context["emp"] = emp
    context["id"] = id
    return render(request, "timesheet/timesheet.html", context)



@login_required(login_url='/home/')
def update_status(request, id, status):
    emp = catalogModel.Employee.objects.filter(user__username__exact = request.user.username).first()
    context ={}

    obj = get_object_or_404(Timesheet, id = id)
    
    if obj:
        obj.updatedBy = request.user.username
        obj.updated_date = datetime.now()    
        obj.Status = status
        obj.save()
        # Return to Locations List
        return HttpResponseRedirect('/timesheet/employee_list/')

         
    context["emp"] = emp
    context["id"] = id
    return render(request, "timesheet/timesheet.html/" + str(id), context)


"""
**************** SUPERVISOR *********************************
"""

@login_required(login_url='/home/')
def supervisor_list(request):
    emp = catalogModel.Employee.objects.filter(user__username__exact = request.user.username).first()
    context ={}
    estatus = "0"

    if request.method == "POST":
        estatus = request.POST.get('status')
       
    
    context["selectEstatus"] = estatus    

    if estatus == "0":
        ts = Timesheet.objects.filter(Status__in =  (2,3), Location = emp.Location)
    else:
        ts = Timesheet.objects.filter(Status = estatus , Location = emp.Location)

    
    context["dataset"] = ts
    
    context["emp"]= emp

    return render(request, "timesheet/supervisor_list.html", context)


@login_required(login_url='/home/')
def createBySupervisor(request):
    emp = catalogModel.Employee.objects.filter(user__username__exact = request.user.username).first()
    context ={}

    form = TimesheetSuperForm(request.POST or None)

    if form.is_valid():
        form.instance.createdBy = request.user.username
        form.instance.created_date = datetime.now()    
        form.save()
        # Return to Locations List
        return HttpResponseRedirect('/timesheet/supervisor_list/')

         
    context['form']= form
    context["emp"] = emp
    return render(request, "timesheet/supervisor_timesheet.html", context)

@login_required(login_url='/home/')
def updateBySuper(request, id):
    emp = catalogModel.Employee.objects.filter(user__username__exact = request.user.username).first()
    context ={}

    obj = get_object_or_404(Timesheet, id = id)

    if obj.Status == 4:
        form = TimesheetSuperFormApproved(request.POST or None, instance = obj)
    else:
        form = TimesheetSuperForm(request.POST or None, instance = obj)

    if form.is_valid():
    
        if request.POST.get('newstatus') != '' :
                form.instance.Status = request.POST.get('newstatus')

        form.instance.updatedBy = request.user.username
        form.instance.updated_date = datetime.now()    
        form.save()
        # Return to Locations List
        return HttpResponseRedirect('/timesheet/supervisor_list/')

         
    context['obj']= obj
    context['form']= form
    context["emp"] = emp
    context["id"] = id
    return render(request, "timesheet/supervisor_timesheet.html", context)



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