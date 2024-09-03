from django import forms
from django.forms.models import model_to_dict
# from .models import stratIndicator, RefStratArea, RefStratObj, RefStratPlan,strategic, stratDetArea, stratDetObj,stratDet, ludip
from .models import *

#ludip

class ludipForm(forms.ModelForm):
    class Meta:
        model = ludip
        fields = ['campus','totalLandArea', 'landUsed','remainLand', 'landUsedMap', 'siteDevPlan','remarks']

        widgets = {
            'campus':forms.TextInput(attrs={'class':'form-control','style':'margin-bottom:10px'}),
            'totalLandArea':forms.TextInput(attrs={'class':'form-control', 'style':'margin-bottom:10px'}),
            'landUsed':forms.TextInput(attrs={'class':'form-control','style':'margin-bottom:10px'}),
            'remainLand':forms.TextInput(attrs={'class':'form-control','style':'margin-bottom:10px'}),
            'landUsedMap':forms.TextInput(attrs={'class':'form-control','style':'margin-bottom:10px'}),
            'siteDevPlan':forms.TextInput(attrs={'class':'form-control','style':'margin-bottom:10px'}),
            'remarks':forms.Textarea(attrs={'rows':'4', 'class':'form-control', 'style':'margin-bottom:10px'})
        }
