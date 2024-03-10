from typing import Any
from django.contrib.auth.models import User
from django import forms
from .models import CustomBaseuser


class update_customer(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))    
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))    
    class Meta:
        model = CustomBaseuser
        fields =['email','firstname','lastname']
        

class create_customer(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))    
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))    
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))    
    
    class Meta:
        model = CustomBaseuser
        fields =['email','password','firstname','lastname']
 