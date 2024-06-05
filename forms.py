from typing import Any
from django import forms
from secondapp.models import Employee
# Register your forms here.
class student(forms.Form):
    Stu_Id=forms.IntegerField()
    Stu_Name=forms.CharField(max_length=110)
    Stu_Class=forms.IntegerField()
    Stu_F_Name=forms.CharField(max_length=110)
    Stu_Address=forms.CharField(max_length=110)
    passWord=forms.CharField(max_length=110)
    R_passWord=forms.CharField(max_length=110)
    P_number=forms.CharField(max_length=10)

    def clean(self):
        print("inside clean ")
        a=super().clean()
        c=a['passWord']
        K=a['R_passWord']
        if(c != K):
            raise forms.ValidationError("Enter a Correct Password")

class Emp_data(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"   