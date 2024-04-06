from typing import Any
from django.contrib.auth.models import User
from django import forms
from .models import CustomBaseuser


class update_customer(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))    
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))    
    # birth_date = forms.CharField(widget=forms.DateInput(attrs={'class': 'form-control'}))    
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))    
    # profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))    

    class Meta:
        model = CustomBaseuser
        fields =['email','firstname','lastname','phone_number']
        

class create_customer(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))    
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))    
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))    
    
    class Meta:
        model = CustomBaseuser
        fields =['email','password','firstname','lastname']
 