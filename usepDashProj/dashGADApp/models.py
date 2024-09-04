from django.db import models

# Create your models here.


#campus 
class gadCampus(models.Model):
    campId = models.AutoField(primary_key=True, editable=True)
    name = models.CharField(max_length=50)
    IsActive = models.CharField(max_length=1, default='Y')
    
    class Meta:
        db_table = "man_campus"
    
#division 
class gadDivision(models.Model):
    divId = models.AutoField(primary_key=True, editable=True)
    campId = models.CharField(max_length=20, default = '')
    name = models.CharField(max_length=150)
    isActive = models.CharField(max_length=1, default='Y')

    class Meta:
        db_table = "man_division"

#Component 
class gadComponent(models.Model):
    compId = models.AutoField(primary_key=True, editable=True)
    divId = models.CharField(max_length=20)
    description = models.CharField(max_length=250)
    isActive = models.CharField(max_length=1, default='Y')

    class Meta:
        db_table = "man_component"


class gadDetails(models.Model):
    gadId = models.AutoField(primary_key=True,editable=True)
    campId = models.CharField(max_length=20)
    compId = models.CharField(max_length=20)
    series = models.CharField(max_length=100)
    program = models.CharField(max_length=150)
    female = models.CharField(max_length=20)
    male = models.CharField(max_length=20)
    total = models.CharField(max_length=20)
    isActive = models.CharField(max_length=1, default='Y')

    class Meta:
        db_table = "gad"