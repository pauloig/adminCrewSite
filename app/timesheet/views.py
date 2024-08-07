from ast import Try, parse
from django.shortcuts import render, redirect
from django.http import HttpResponse
import xlwt
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

    
    context["dataset"] = Timesheet.objects.filter(EmployeeID = emp, Status__in = (1,5)).order_by('-date').values()
    
    context["emp"]= emp

    return render(request, "timesheet/employee_list.html", context)

@login_required(login_url='/home/')
def employee_submitted_list(request):
    emp = catalogModel.Employee.objects.filter(user__username__exact = request.user.username).first()
    context ={}

    
    context["dataset"] = Timesheet.objects.filter(EmployeeID = emp, Status__in = (2,3,4)).order_by('-date').values()
    
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

        if request.POST.get('newstatus') != '' :
            form.instance.Status = request.POST.get('newstatus')

        if request.POST.get('newTotalM') != '' :    
            form.instance.total_mileage = request.POST.get('newTotalM')
        else:
            form.instance.total_mileage = 0

        form.instance.total_mileage = validate_decimals(validate_decimals(form.cleaned_data["end_mileage"]) - validate_decimals(form.cleaned_data["start_mileage"]))
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

        form.instance.total_mileage = validate_decimals(validate_decimals(form.instance.end_mileage) - validate_decimals(form.instance.start_mileage))
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


"""
****************  REPORTS *********************************
"""
@login_required(login_url='/home/')
def report_list(request):
    
    context ={}
    emp = catalogModel.Employee.objects.filter(user__username__exact = request.user.username).first()
    context["emp"]= emp

    if request.method == "POST":
        dateSelected =  request.POST.get('date')
        dateSelected2 = request.POST.get('date2')
        dateS = datetime.strptime(dateSelected, '%Y-%m-%d').date()
        dateS2 = datetime.strptime(dateSelected2, '%Y-%m-%d').date()
        status = request.POST.get('status')        
        
           

        if status == "0":
            ts = Timesheet.objects.filter(date__range=[dateS, dateS2])
        else:
            ts = Timesheet.objects.filter(Status = status , date__range=[dateS, dateS2])

        
        context["dataset"] = ts
        context["selectEstatus"] = status 
        context["dateSelected"] =  dateS
        context["dateSelected2"] =  dateS2


    return render(request, "timesheet/report_list.html", context)


@login_required(login_url='/home/')
def get_report_list(request, dateSelected, dateSelected2, status):
    

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('employee-report', cell_overwrite_ok = True) 

    

    # Sheet header, first row
    row_num = 4

    font_title = xlwt.XFStyle()
    font_title.font.bold = True
    font_title = xlwt.easyxf('font: bold on, color black;\
                     borders: top_color black, bottom_color black, right_color black, left_color black,\
                              left thin, right thin, top thin, bottom thin;\
                     pattern: pattern solid, fore_color gray25;')

    
    font_style =  xlwt.XFStyle()              

    font_title2 = xlwt.easyxf('font: bold on, color black;\
                                align: horiz center;\
                                pattern: pattern solid, fore_color gray25;')

    dateS = datetime.strptime(dateSelected, '%Y-%m-%d').date()
    dateS2 = datetime.strptime(dateSelected2, '%Y-%m-%d').date()
    
                              
    ws.write_merge(3, 3, 0, 10, 'Employee Report ' + str(datetime.strftime(dateS, "%m/%d/%Y")) + ' - ' + str(datetime.strftime(dateS2, "%m/%d/%Y")),font_title2)   


                   

    columns = ['Date', 'Name', 'Location', 'Clock In', 'Lunch Start','Lunch End','Clock Out', 'Starting Mileage','Ending Mileage','Total Mileage','Status' ] 

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_title) # at 0 row 0 column 
      

    
    #ordenes = woInvoice.objects.filter(created_date__year = datetime.strftime(dateS, '%Y'), created_date__month = datetime.strftime(dateS, '%m'))
    if status == "0":
        ts = Timesheet.objects.filter(date__range=[dateS, dateS2])
    else:
        ts = Timesheet.objects.filter(Status = status , date__range=[dateS, dateS2])
       
    for item in ts:
        row_num += 1
        ws.write(row_num, 0, item.date.strftime("%m/%d/%Y"), font_style) # at 0 row 0 column 
        ws.write(row_num, 1, str(item.EmployeeID.employeeID) + ' - ' + item.EmployeeID.first_name + ' ' + item.EmployeeID.last_name , font_style) # at 0 row 0 column  
        ws.write(row_num,2, item.Location.LocationID + '-' + item.Location.name, font_style) # at 0 row 0 column        
        ws.write(row_num, 3, item.start_time, font_style)
        ws.write(row_num, 4, item.start_lunch_time, font_style)
        ws.write(row_num, 5, item.end_lunch_time, font_style)
        ws.write(row_num, 6, item.end_time, font_style)
        ws.write(row_num, 7, item.start_mileage, font_style)
        ws.write(row_num, 8, item.end_mileage, font_style)
        ws.write(row_num, 9, item.total_mileage, font_style)

        if item.Status == 1:
            ws.write(row_num, 10, 'Draft', font_style)
        elif item.Status == 2:
            ws.write(row_num, 10, 'Sent', font_style)
        elif item.Status == 3:
            ws.write(row_num, 10, 'Pending', font_style)
        elif item.Status == 4:
            ws.write(row_num, 10, 'Approved', font_style)
        elif item.Status == 5:
            ws.write(row_num, 10, 'Rejected', font_style)


    ws.col(1).width = 12000
    ws.col(2).width = 6000
    ws.col(3).width = 3000
    ws.col(4).width = 3000
    ws.col(5).width = 3000
    ws.col(6).width = 3000
    ws.col(7).width = 4000
    ws.col(8).width = 4000
    ws.col(9).width = 4000
    ws.col(10).width = 7000
    ws.col(11).width = 6000
    ws.col(12).width = 3000
    ws.col(13).width = 6000

    filename = 'Employee report ' + dateSelected + '.xls'
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=' + filename 

    wb.save(response)

    return response

"""
****************  UTILIDADES *********************************
"""
def validate_decimals(value):
    try:
        return round(float(str(value)), 2)
    except:
       return 0