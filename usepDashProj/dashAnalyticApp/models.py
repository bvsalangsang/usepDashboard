from django.db import models

# Create your models here.

# universal for all app*
# reference type : outcome and output

class refType(models.Model):
    typeNo = models.AutoField(primary_key=True, editable=True)
    description = models.CharField(max_length=100)
    isActive = models.CharField(max_length=1, default='Y')

    class Meta:
        db_table = "ref_type"

#Analytics
class analytics(models.Model):
    analId = models.AutoField(primary_key=True, editable=True)
    progId = models.CharField(max_length=20,default='')
    typeNo = models.CharField(max_length=20)
    indicator = models.CharField(max_length=500)
    isActive = models.CharField(max_length=1, default='Y') 

    class Meta:
        db_table = "analytics"
     
class analIndicator(models.Model):
    analIndId = models.AutoField(primary_key=True, editable=True)
    analId = models.CharField(max_length=20)
    colDescription =  models.CharField(max_length=500)
    isActive = models.CharField(max_length=1, default='Y') 

    class Meta:
        db_table = "anal_indicator"

class analIndicatorDet(models.Model):
    ctrlNo = models.AutoField(primary_key=True, editable=True)
    analIndId = models.CharField(max_length=20)
    year = models.CharField(max_length=20)
    value = models.CharField(max_length=100)
    isActive = models.CharField(max_length=1, default='Y')  
    
    class Meta:
        db_table = "anal_indicator_det"

class analPrograms(models.Model):
    progId = models.AutoField(primary_key=True, editable=True)
    name = models.CharField(max_length=250)
    isActive = models.CharField(max_length=1, default='Y')

    class Meta:
        db_table = "anal_program"

# analytics indicator - Board passers
class analBoardPassers(models.Model):
    ctrlNo = models.AutoField(primary_key=True, editable=True)
    analId = models.CharField(max_length=20)
    year = models.CharField(max_length=20)
    noOfTakers = models.CharField(max_length=100)
    noOfPassers = models.CharField(max_length=100)
    percentage = models.CharField(max_length=100)
    isActive = models.CharField(max_length=1, default='Y')  
    
    class Meta:
        db_table = "anal_board_passers"

# analytics indicator - Employability
class analEmployability(models.Model):
    ctrlNo = models.AutoField(primary_key=True, editable=True)
    analId = models.CharField(max_length=20)
    year = models.CharField(max_length=20)
    noOfGrads = models.CharField(max_length=100)
    noOfEmployed = models.CharField(max_length=100)
    percentage = models.CharField(max_length=100)
    isActive = models.CharField(max_length=1, default='Y')  
    
    class Meta:
        db_table = "anal_employability"

# analytics indicator - Employability
class analChedRdcIdent(models.Model):
    ctrlNo = models.AutoField(primary_key=True, editable=True)
    analId = models.CharField(max_length=20)
    year = models.CharField(max_length=20)
    noOfUnderGrad = models.CharField(max_length=100)
    noOfChedRdcIdent = models.CharField(max_length=100)
    percentage = models.CharField(max_length=100)
    isActive = models.CharField(max_length=1, default='Y')  
    
    class Meta:
        db_table = "anal_ched_rdc"

# analytics indicator - Accreditation
class analAccreditation(models.Model):
    ctrlNo = models.AutoField(primary_key=True, editable=True)
    analId = models.CharField(max_length=20)
    year = models.CharField(max_length=20)
    noOfUnderGradProg = models.CharField(max_length=100)
    noOfUnderGradProgAccred = models.CharField(max_length=100)
    percentage = models.CharField(max_length=100)
    isActive = models.CharField(max_length=1, default='Y')  
    
    class Meta:
        db_table = "anal_accreditation"

# analytics indicator - faculty research
class analGradResearch(models.Model):
    ctrlNo = models.AutoField(primary_key=True, editable=True)
    analId = models.CharField(max_length=20)
    year = models.CharField(max_length=20)
    noOfGradFac = models.CharField(max_length=100)
    noOfGradFacRes = models.CharField(max_length=100)
    percentage = models.CharField(max_length=100)
    isActive = models.CharField(max_length=1, default='Y')  
    
    class Meta:
        db_table = "anal_grad_research"


# analytics indicator - Research degree
class analResDegree(models.Model):
    ctrlNo = models.AutoField(primary_key=True, editable=True)
    analId = models.CharField(max_length=20)
    year = models.CharField(max_length=20)
    noOfGrad = models.CharField(max_length=100)
    noOfGradResDeg = models.CharField(max_length=100)
    percentage = models.CharField(max_length=100)
    isActive = models.CharField(max_length=1, default='Y')  
    
    class Meta:
        db_table = "anal_res_degree"

# analytics indicator - Accredited Graduate Program
class analAccGradProg(models.Model):
    ctrlNo = models.AutoField(primary_key=True, editable=True)
    analId = models.CharField(max_length=20)
    year = models.CharField(max_length=20)
    noOfGradProg = models.CharField(max_length=100)
    noOfAccrGradProg= models.CharField(max_length=100)
    percentage = models.CharField(max_length=100)
    isActive = models.CharField(max_length=1, default='Y')  
    
    class Meta:
        db_table = "anal_accr_grad_prog"  

# analytics indicator - Research Output
class analResOutput(models.Model):
    ctrlNo = models.AutoField(primary_key=True, editable=True)
    analId = models.CharField(max_length=20)
    year = models.CharField(max_length=20)
    noOfResOutput = models.CharField(max_length=100)
    isActive = models.CharField(max_length=1, default='Y')  
    
    class Meta:
        db_table = "anal_res_output"  

# analytics indicator - Research Output Completed
class analResComplete(models.Model):
    ctrlNo = models.AutoField(primary_key=True, editable=True)
    analId = models.CharField(max_length=20)
    year = models.CharField(max_length=20)
    noOfResComplete = models.CharField(max_length=100)
    isActive = models.CharField(max_length=1, default='Y')  
    
    class Meta:
        db_table = "anal_res_complete"  


# analytics indicator - Research Output Completed
class analResPublished(models.Model):
    ctrlNo = models.AutoField(primary_key=True, editable=True)
    analId = models.CharField(max_length=20)
    year = models.CharField(max_length=20)
    noOfResOutput = models.CharField(max_length=100)
    noOfResPublished= models.CharField(max_length=100)
    percentage = models.CharField(max_length=100)
    isActive = models.CharField(max_length=1, default='Y')  
    
    
    class Meta:
        db_table = "anal_res_published"  

# analytics indicator - Active partnership
class analActPartner(models.Model):
    ctrlNo = models.AutoField(primary_key=True, editable=True)
    analId = models.CharField(max_length=20)
    year = models.CharField(max_length=20)
    noOfActPart = models.CharField(max_length=100)
    isActive = models.CharField(max_length=1, default='Y')  
    
    class Meta:
        db_table = "anal_active_partner"  

# analytics indicator - Number of Trainess
class analTrainees(models.Model):
    ctrlNo = models.AutoField(primary_key=True, editable=True)
    analId = models.CharField(max_length=20)
    year = models.CharField(max_length=20)
    noOfTrainees = models.CharField(max_length=100)
    isActive = models.CharField(max_length=1, default='Y')  
    
    class Meta:
        db_table = "anal_num_trainees"  

# analytics indicator - Number of Extension Program
class analExtProgram(models.Model):
    ctrlNo = models.AutoField(primary_key=True, editable=True)
    analId = models.CharField(max_length=20)
    year = models.CharField(max_length=20)
    noOfExtProgram = models.CharField(max_length=100)
    isActive = models.CharField(max_length=1, default='Y')  
    
    class Meta:
        db_table = "anal_ext_program"  


class analBeneficiaries(models.Model):
    ctrlNo = models.AutoField(primary_key=True, editable=True)
    analId = models.CharField(max_length=20)
    year = models.CharField(max_length=20)
    noOfBenef = models.CharField(max_length=100)
    noOfBenefRate= models.CharField(max_length=100)
    percentage = models.CharField(max_length=100)
    isActive = models.CharField(max_length=1, default='Y')  
    
    class Meta:
        db_table = "anal_beneficiaries"  
