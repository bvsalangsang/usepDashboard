from django import forms

from .models import *

#campus
class campusForm(forms.ModelForm):
    class Meta:
        model = gadCampus
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'style':'margin-bottom:10px'})
        }

class divisionForm(forms.ModelForm):
    class Meta:
        model = gadDivision
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'style':'margin-bottom:10px'})
        }


class componentForm(forms.ModelForm):
    class Meta:
        model = gadComponent
        fields = ['description']
        widgets = {
            'description': forms.TextInput(attrs={'class':'form-control', 'style':'margin-bottom:10px'})
        }

class gadForm(forms.ModelForm):
    class Meta:
        model = gadDetails
        fields = ['series','program','female','male','total']
        widgets = {
            'series': forms.TextInput(attrs={'class':'form-control', 'style':'margin-bottom:10px'}),
            'program': forms.TextInput(attrs={'class':'form-control', 'style':'margin-bottom:10px'}),
            'female': forms.TextInput(attrs={'class':'form-control', 'style':'margin-bottom:10px'}),
            'male': forms.TextInput(attrs={'class':'form-control', 'style':'margin-bottom:10px'}),
            'total': forms.TextInput(attrs={'class':'form-control', 'style':'margin-bottom:10px'}),
   }        
