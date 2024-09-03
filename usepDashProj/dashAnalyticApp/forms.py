from django import forms
from django.forms.models import model_to_dict
# from .models import stratIndicator, RefStratArea, RefStratObj, RefStratPlan,strategic, stratDetArea, stratDetObj,stratDet, ludip
from .models import *


#analytics
class analyticsForm(forms.ModelForm):
    class Meta:
        model = analytics
        fields = ['indicator']

        widgets = {
            'indicator':forms.Textarea(attrs={'rows':'4', 'class':'form-control', 'style':'margin-bottom:10px'})
        }

class analIndForm(forms.ModelForm):
    class Meta:
        model = analIndicator
        fields = ['colDescription']

        widgets = {
            'colDescription':forms.Textarea(attrs={'rows':'4', 'class':'form-control', 'style':'margin-bottom:10px'})
        }

#analytics indicator board passer

class analBPForm(forms.ModelForm):
    class Meta:
        model = analBoardPassers
        fields = ['year','noOfTakers', 'noOfPassers','percentage']
        widgets = {
                'year':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
                'noOfTakers':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
                'noOfPassers':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
                'percentage':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'})
            }

#analytics indicator employability
class analEmployForm(forms.ModelForm):
    class Meta:
        model = analEmployability
        fields = ['year','noOfGrads', 'noOfEmployed','percentage']
        widgets = {
                'year':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
                'noOfGrads':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
                'noOfEmployed':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
                'percentage':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'})
            }

#analytics indicator employability
class analChedRdcForm(forms.ModelForm):
    class Meta:
        model = analChedRdcIdent
        fields = ['year','noOfUnderGrad', 'noOfChedRdcIdent','percentage']
        widgets = {
                'year':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
                'noOfUnderGrad':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
                'noOfChedRdcIdent':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
                'percentage':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'})
            }
        
#analytics indicator accreditation
class analAccredForm(forms.ModelForm):
    class Meta:
        model = analAccreditation
        fields = ['year','noOfUnderGradProg', 'noOfUnderGradProgAccred','percentage']
        widgets = {
                'year':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
                'noOfUnderGradProg':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
                'noOfUnderGradProgAccred':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
                'percentage':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'})
            }

class analGradResForm(forms.ModelForm):
    class Meta:
        model = analGradResearch
        fields = ['year','noOfGradFac', 'noOfGradFacRes','percentage']
        widgets = {
                'year':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
                'noOfGradFac':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
                'noOfGradFacRes':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
                'percentage':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'})
            }
    
class analResDegForm(forms.ModelForm):
    class Meta:
        model = analResDegree
        fields = ['year','noOfGrad', 'noOfGradResDeg','percentage']
        widgets = {
                'year':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
                'noOfGrad':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
                'noOfGradResDeg':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
                'percentage':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'})
            }
        
class analAccrGradProgForm(forms.ModelForm):
    class Meta:
        model = analAccGradProg
        fields = ['year','noOfGradProg', 'noOfAccrGradProg','percentage']
        widgets = {
                'year':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
                'noOfGradProg':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
                'noOfAccrGradProg':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
                'percentage':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'})
            }
        
class analResOutputForm(forms.ModelForm):
    class Meta:
        model = analResOutput
        fields = ['year','noOfResOutput']
        widgets = {
                'year':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
                'noOfResOutput':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
            }
        
        
class analResCompleteForm(forms.ModelForm):
    class Meta:
        model = analResComplete
        fields = ['year','noOfResComplete']
        widgets = {
                'year':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
                'noOfResComplete':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
            }

class analResPublishedForm(forms.ModelForm):
    class Meta:
        model = analResPublished
        fields = ['year','noOfResOutput', 'noOfResPublished','percentage']
        widgets = {
                'year':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
                'noOfResOutput':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
                'noOfResPublished':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
                'percentage':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'})
            }
        
        
class analActPartnerForm(forms.ModelForm):
    class Meta:
        model = analActPartner
        fields = ['year','noOfActPart']
        widgets = {
                'year':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
                'noOfActPart':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
            }

         
class analTraineesForm(forms.ModelForm):
    class Meta:
        model = analTrainees
        fields = ['year','noOfTrainees']
        widgets = {
                'year':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
                'noOfTrainees':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
            }
               
         
class analExtProgramForm(forms.ModelForm):
    class Meta:
        model = analExtProgram
        fields = ['year','noOfExtProgram']
        widgets = {
                'year':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
                'noOfExtProgram':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
            }
               
class analBeneficiaryForm(forms.ModelForm):
    class Meta:
        model = analBeneficiaries
        fields = ['year','noOfBenef', 'noOfBenefRate','percentage']
        widgets = {
                'year':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
                'noOfBenef':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
                'noOfBenefRate':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'}),
                'percentage':forms.TextInput(attrs={'class':'form-control', 'placeholder':'', 'style':'margin-bottom:10px'})
            }
        