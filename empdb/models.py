from django.db import models

class Departments(models.Model):
    DepartmentID = models.AutoField(primary_key=True)
    DepartmentName= models.CharField(max_length=500)
class Employees(models.Model):
    EmployeeID = models.AutoField(primary_key=True)
    EmployeeName= models.CharField(max_length=500)
    Department=models.CharField(max_length=500)
    DateOfJoining= models.DateField()
    PhotoFileName = models.CharField(max_length=500)
