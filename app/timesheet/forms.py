import re
from types import CoroutineType
from django import forms
from .models import *

class TimesheetForm(forms.ModelForm):   



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
            'Status', 
            'createdBy',
            'created_date',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['EmployeeID'].disabled = True
        self.fields['Status'].disabled = True