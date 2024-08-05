import re
from types import CoroutineType
from django import forms
from .models import *

class TimesheetForm(forms.ModelForm):   
    class Meta:
        model = Timesheet
        fields = [
            'id',
            'EmployeeID',
            'date',
            'start_time',
            'start_lunch_time',
            'end_lunch_time',
            'end_time',
            'start_mileage',
            'end_mileage',
            'total_mileage',
            'Location',
            'Status', 
            'createdBy',
            'created_date',
            'updated_date',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['EmployeeID'].disabled = True
        self.fields['Status'].disabled = True
        self.fields['createdBy'].disabled = True
        self.fields['created_date'].disabled = True
        self.fields['updated_date'].disabled = True
        self.fields['total_mileage'].disabled = True
        
class TimesheetDisabledForm(forms.ModelForm):   
    class Meta:
        model = Timesheet
        fields = [
            'id',
            'EmployeeID',
            'date',
            'start_time',
            'start_lunch_time',
            'end_lunch_time',
            'end_time',
            'start_mileage',
            'end_mileage',
            'total_mileage',
            'Location',
            'Status', 
            'createdBy',
            'created_date',
            'updated_date',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['EmployeeID'].disabled = True
        self.fields['date'].disabled = True
        self.fields['start_time'].disabled = True
        self.fields['start_lunch_time'].disabled = True
        self.fields['end_lunch_time'].disabled = True
        self.fields['end_time'].disabled = True
        self.fields['start_mileage'].disabled = True
        self.fields['end_mileage'].disabled = True
        self.fields['total_mileage'].disabled = True
        self.fields['Location'].disabled = True
        self.fields['Status'].disabled = True
        self.fields['createdBy'].disabled = True
        self.fields['created_date'].disabled = True
        self.fields['updated_date'].disabled = True
        self.fields['total_mileage'].disabled = True

class TimesheetSuperForm(forms.ModelForm):   
    class Meta:
        model = Timesheet
        fields = [
            'EmployeeID',
            'date',
            'start_time',
            'start_lunch_time',
            'end_lunch_time',
            'end_time',
            'start_mileage',
            'end_mileage',
            'total_mileage',
            'Location',
            'Status', 
            'createdBy',
            'created_date',
            'updated_date',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['createdBy'].disabled = True
        self.fields['created_date'].disabled = True
        self.fields['updated_date'].disabled = True

class TimesheetSuperFormApproved(forms.ModelForm):   
    class Meta:
        model = Timesheet
        fields = [
            'EmployeeID',
            'date',
            'start_time',
            'start_lunch_time',
            'end_lunch_time',
            'end_time',
            'start_mileage',
            'end_mileage',
            'total_mileage',
            'Location',
            'Status', 
            'createdBy',
            'created_date',
            'updated_date',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['EmployeeID'].disabled = True
        self.fields['date'].disabled = True
        self.fields['start_time'].disabled = True
        self.fields['start_lunch_time'].disabled = True
        self.fields['end_lunch_time'].disabled = True
        self.fields['end_time'].disabled = True
        self.fields['start_mileage'].disabled = True
        self.fields['end_mileage'].disabled = True
        self.fields['total_mileage'].disabled = True
        self.fields['Location'].disabled = True
        self.fields['Status'].disabled = True
        self.fields['createdBy'].disabled = True
        self.fields['created_date'].disabled = True
        self.fields['updated_date'].disabled = True