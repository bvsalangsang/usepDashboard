from django import forms
from django.forms.models import model_to_dict
from .models import *


class stratAreaForm(forms.ModelForm):
    class Meta:
        model = stratArea

        fields = ['code','name']
 
        widgets = {
            'code':forms.TextInput(attrs={'class':'form-control','style':'margin-bottom:10px'}),
            'name':forms.TextInput(attrs={'class':'form-control', 'style':'margin-bottom:10px'}),
            }

class stratObjForm(forms.ModelForm):
    class Meta:
        model = stratObjective

        fields = ['code','description']
 
        widgets = {
            'code':forms.TextInput(attrs={'class':'form-control','style':'margin-bottom:10px'}),
            'description':forms.TextInput(attrs={'class':'form-control', 'style':'margin-bottom:10px'}),
            }
        
class stratIndForm(forms.ModelForm):
    class Meta:
        model = stratIndicator

        fields = ['code','description']
 
        widgets = {
            'code':forms.TextInput(attrs={'class':'form-control','style':'margin-bottom:10px'}),
            'description':forms.TextInput(attrs={'class':'form-control', 'style':'margin-bottom:10px'}),
            }

class stratTempForm(forms.ModelForm):
    class Meta:
        model = stratTemplate
        fields = ['tempId','tempName']
        widgets = {
        'tempId':forms.TextInput(attrs={'class':'form-control','style':'margin-bottom:10px'}),
        'tempName':forms.TextInput(attrs={'class':'form-control', 'style':'margin-bottom:10px'}),
        }

class  stratRefForm(forms.ModelForm):
    class Meta:
        model = stratReference
        fields = ['refName','description']
        widgets = {
            'refName':forms.TextInput(attrs={'class':'form-control','style':'margin-bottom:10px'}),
            'description':forms.TextInput(attrs={'class':'form-control', 'style':'margin-bottom:10px'}),
        }
