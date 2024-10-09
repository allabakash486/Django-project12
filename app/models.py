from django.db import models

# Create your models here.
class Dept(models.Model):
    Dept_no = models.IntegerField(max_length=5,primary_key=True)
    Dept_name = models.CharField(max_length=100)
    Dept_Loc = models.CharField(max_length=20)
class Employee(models.Model):
    Emp_no = models.PositiveIntegerField(max_length=5,primary_key=True)
    Emp_name = models.CharField(max_length=100)
    Emp_Designation = models.CharField(max_length=50)
    Emp_Salary = models.IntegerField()
    dept_no =models.ForeignKey(Dept,on_delete=models.CASCADE)
class country(models.Model):
    country_id = models.PositiveBigIntegerField(max_length=5,primary_key=True)
    country_name = models.CharField(max_length=20)
class Country_capital(models.Model):
    Capital_id = models.PositiveBigIntegerField(max_length=4,primary_key=True)
    capital_name = models.OneToOneField(country,on_delete=models.CASCADE)
