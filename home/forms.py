from django import forms
from django.forms import widgets
from .models import crms
from django.core import validators


class StudentRegistration(forms.ModelForm):
    class Meta:
        model=crms
        fields=['id','description','assigned_user_id']
        widgets={
         'id':forms.TextInput(attrs={'class':'form-control'}),
         'description':forms.TextInput(attrs={'class':'form-control'}),
         'assigned_user_id':forms.TextInput(attrs={'class':'form-control'}),
        }
