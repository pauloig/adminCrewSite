import re
from types import CoroutineType
from django import forms
from .models import *

class EmployeesForm(forms.ModelForm):   

    employeeID = forms.CharField(required=False)

    class Meta:
        model = Employee
        fields = [
            "employeeID",
            "first_name",           
            "last_name",
             "middle_initial",
             "termination_date",
             "hire_created",
             "hourly_rate",
             "email",
             "Location",
             "user",
             "is_active",
             "is_supervisor",
             "is_admin",
             "is_hr",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['employeeID'].disabled = True


class LocationForm(forms.ModelForm):   
    LocationID = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class':'form-control'}))
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(max_length=150, widget=forms.Textarea(attrs={'class':'form-control'}))
    city= forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    is_active= forms.BooleanField(required=False)

    class Meta:
        model = Location
        fields = [
            "LocationID",
            "name",           
            "description",
             "city",
             'is_active'
             
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
 