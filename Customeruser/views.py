from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import EmailMessage, get_connection
from django.conf import Settings
from .custom_token import Token_Customizer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny, IsAuthenticated
import json

from .models import *
from .serializer import *
from .tasks import *

class User_create(APIView,):
    permission_classes = [AllowAny,]
    # parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        print(request.data)
        try:
            existing_user = CustomBaseuser.objects.get(
                email=request.data['email'])
            return Response({'message': 'User already exists !!!!'})
        except:
            pass
        user = User_serializer(data=request.data)
        if user.is_valid(raise_exception=True):
            newuser = user.save()
            token = Token_Customizer.get_token(newuser)
            serialized_token = json.dumps(str(token))
            subject = 'Verify Your Email'
            from_email = 'nwekelesley@gmail.com'
            to = newuser.email
            send_email_task.delay(
                subject, from_email, serialized_token, to)
            print('here1')
            if newuser:
                return Response({'message': 'Successful'}, status=status.HTTP_201_CREATED)

        return Response(User_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request):
        data=request.data
        try:
            user_to_be_updated = CustomBaseuser.objects.get(email=data['email'])
            try:     
                data['email'],data['firstname'],data['lastname'],data['birth_date'],
                data['phone_number'],data['profile_pic']
                user_to_be_updated.email=data['email']
                user_to_be_updated.firstname=data['firstname']
                user_to_be_updated.lastname=data['lastname']
                user_to_be_updated.birth_date=data['birth_date']
                user_to_be_updated.phone_number=data['phone_number']
                user_to_be_updated.profile_pic=data['profile_pic']
                user_to_be_updated.save()
                return Response({'message':'Updated'})
            except:
                return Response({'message':'Check your data'})
        except:
            return Response({'message':'Please sign_up as a user'})

