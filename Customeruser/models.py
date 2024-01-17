from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, firstname, lastname, password=None):
        if firstname is None:
            raise ValueError('User should have a username')
        if lastname is None:
            raise ValueError('Please fill lastname')
        if email is None:
            raise ValueError(_('Please provide an email'))
        email = self.normalize_email(email)
        user = self.model(email=email, firstname=firstname, lastname=lastname)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, firstname, lastname, password=None):

        user = self.create_user(email, firstname, lastname, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user
    
class CustomBaseuser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    firstname = models.CharField(max_length=150, blank=False)
    lastname = models.CharField(max_length=150, blank=False)
    birth_date = models.DateField(blank=False, null=True)
    joined_date = models.DateTimeField(auto_now_add=True, null=True)
    phone_number = models.IntegerField(blank=False, null=True)
    profile_pic = models.ImageField(
        upload_to='images', default="/variac.jpeg/", blank=True, null=True)
    email_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname']

    def __str__(self):
        return f'{self.lastname}:{self.firstname}'