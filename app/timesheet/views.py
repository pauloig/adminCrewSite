from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth import authenticate, login as login_process
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from .models import *
#from .forms import * 
from . import views
from sequences import get_next_value, Sequence

@login_required(login_url='/home/')
def employee_list(request):
    emp = catalogModel.Employee.objects.filter(user__username__exact = request.user.username).first()
    context ={}

    
    context["dataset"] = Timesheet.objects.filter(EmployeeID = emp)
    
    context["emp"]= emp

    return render(request, "timesheet/employee_list.html", context)

