from django.db import models

# Create your models here.

# LUDIP 
class ludip(models.Model):
    ludipId = models.AutoField(primary_key=True, editable=True)
    campus = models.CharField(max_length=100,default='')
    totalLandArea = models.CharField(max_length=50)
    landUsed = models.CharField(max_length=50)
    remainLand = models.CharField(max_length=50)
    landUsedMap = models.CharField(max_length=250)
    siteDevPlan = models.CharField(max_length=250)
    remarks = models.CharField(max_length=500)
    isActive = models.CharField(max_length=1, default='Y')

    class Meta:
        db_table = "ludip"

