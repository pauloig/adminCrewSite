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
             "user",
             "is_active",
             "is_supervisor",
             "is_admin",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['employeeID'].disabled = True