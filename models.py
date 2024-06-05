from django.db import models

# Create your models here.
class Employee(models.Model):
    Emp_id=models.AutoField(primary_key=True)
    Emp_Name=models.CharField(max_length=110)
    Dept_Name=models.CharField(max_length=110)
    Roles=models.CharField(max_length=110)
    Emp_Address=models.CharField(max_length=110)