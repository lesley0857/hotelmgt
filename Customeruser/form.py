from typing import Any
from django.contrib.auth.models import User
from django import forms
from .models import CustomBaseuser

class update_picture(forms.ModelForm):
    
    class Meta:
        model = CustomBaseuser
        fields =['profile_pic']

class update_customer(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'border-gray-300 dark:border-gray-700 dark:bg-gray-900 dark:text-gray-300 focus:border-indigo-500 dark:focus:border-indigo-600 focus:ring-indigo-500 dark:focus:ring-indigo-600 rounded-md shadow-sm mt-1 block w-full'}))
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class': 'border-gray-300 dark:border-gray-700 dark:bg-gray-900 dark:text-gray-300 focus:border-indigo-500 dark:focus:border-indigo-600 focus:ring-indigo-500 dark:focus:ring-indigo-600 rounded-md shadow-sm mt-1 block w-full'}))    
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'border-gray-300 dark:border-gray-700 dark:bg-gray-900 dark:text-gray-300 focus:border-indigo-500 dark:focus:border-indigo-600 focus:ring-indigo-500 dark:focus:ring-indigo-600 rounded-md shadow-sm mt-1 block w-full'}))    
    
    # birth_date = forms.CharField(widget=forms.DateInput(attrs={'class': 'form-control'}))    
    # phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))    
    # profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))    

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
 