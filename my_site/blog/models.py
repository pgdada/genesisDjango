from django.db import models

# Create your models here.

from datetime import datetime

class School(models.Model):
    # name
    name = models.CharField(max_length=300)
    # address = models.CharField(max_length=400)
    # zip_code = models.IntegerField()
    def __str__(self) -> str:
        return self.name

class Grade(models.Model):
    # type
    type = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.type

class Certificate(models.Model):
    # name
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name

class Faculty(models.Model):
    # name
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name

class Department(models.Model):
    # name, faculty
    name = models.CharField(max_length=50)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name
    
class Student(models.Model):
    # fullname, grad_year, department, grade, school, certificate_type
    fullname = models.CharField(max_length=100)
    # grad_year = models.IntegerField(default=datetime.today().year)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    grade = models.ForeignKey(Grade, on_delete=models.PROTECT)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    certificate_type = models.ForeignKey(Certificate, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.fullname
 

    # pass
    # school = models.ForeignKey(School, on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # age = models.IntegerField()
    # department = models.CharField(max_length = 50)
    # date_of_resumption = models.DateField(default=datetime.today)

