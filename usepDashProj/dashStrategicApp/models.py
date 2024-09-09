from django.db import models

# Create your models here.

#Area
class stratArea(models.Model):
    areaId = models.AutoField(primary_key=True, editable=True)
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=250)
    isActive = models.CharField(max_length=1, default='Y') 

    class Meta:
        db_table = "man_strat_area"


#Objectives
class stratObjective(models.Model):
    objId = models.AutoField(primary_key=True, editable=True)
    areaId = models.CharField(max_length=20)
    code = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    isActive = models.CharField(max_length=1, default='Y') 

    class Meta:
        db_table = "man_strat_objective"


#Indicator
class stratIndicator(models.Model):
    indId = models.AutoField(primary_key=True, editable=True)
    objId = models.CharField(max_length=20)
    typeNo = models.CharField(max_length=20)
    code = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    isActive = models.CharField(max_length=1, default='Y') 

    class Meta:
        db_table = "man_strat_indicator"


class stratReference(models.Model):
    refNo = models.AutoField(primary_key=True,editable=True)
    refName = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    isActive = models.CharField(max_length=1, default='Y') 

    class Meta:
        db_table = "ref_strat_reference"


#Strategic Plan Matrices 
class stratPlanMatrices(models.Model):
    ctrlNo = models.AutoField(primary_key=True, editable=True)
    indId = models.CharField(max_length=20)
    reference = models.CharField(max_length=20)
    blineData = models.CharField(max_length=30)
    targetPlan = models.CharField(max_length=30)
    yr2022 = models.CharField(max_length=20)
    yr2023 = models.CharField(max_length=20)
    yr2024 = models.CharField(max_length=20)
    yr2025 = models.CharField(max_length=20)
    yr2026 = models.CharField(max_length=20)
    yr2027 = models.CharField(max_length=20)
    isActive = models.CharField(max_length=1, default='Y') 

    class Meta:
        db_table = "strat_plan_matices"

#yearly strategic 
class stratYearlyScorecard(models.Model):
    ctrlNo = models.AutoField(primary_key=True, editable=True)
    indId = models.CharField(max_length=20)
    reference = models.CharField(max_length=30,default='')
    targetyear = models.CharField(max_length=30)
    target = models.CharField(max_length=20)
    actual = models.CharField(max_length=20)
    variance = models.CharField(max_length=20)
    percentage = models.CharField(max_length=20)
    isActive = models.CharField(max_length=1, default='Y') 

    class Meta:
        db_table = "strat_yearly_scorecard"

class stratTemplate(models.Model):
    tempId = models.AutoField(primary_key=True, editable=True)
    tempName = models.CharField(max_length=50)
    createdBy = models.CharField(max_length=20)
    createdDate = models.DateField()
    isActive = models.CharField(max_length=1, default='Y') 

    class Meta:
        db_table = "strat_template"

class stratTemplateDet(models.Model):
    ctrlNo = models.AutoField(primary_key=True, editable=True)
    tempId = models.CharField(max_length=20)
    indId = models.CharField(max_length=20)   
    reference = models.CharField(max_length=30)
    target = models.CharField(max_length=20)
    isActive = models.CharField(max_length=1, default='Y') 

    class Meta:
        db_table = "strat_template_det"