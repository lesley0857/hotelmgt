from django.test import TestCase
import pytest
from django.contrib.auth.models import User
from .models import *
from Customeruser.models import CustomBaseuser, UserManager

# Create your tests here.

# @pytest.fixture()
# def user_1(db):
#     return User.objects.create_user('test_user','les@gmail.com','olodo890')
#coverage run --omit='*/venv/*' manage.py test
#coverage report
#coverage html
# @pytest.mark.django_db
class Test(TestCase):
    def test_User_email(self):
        user = CustomBaseuser.objects.create(email='les@gmail.com',firstname='test_user',lastname='olodo890')
        user.email = "les@gmail.com"
        assert user.email == "les@gmail.com"