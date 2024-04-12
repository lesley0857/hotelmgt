from django.shortcuts import render,redirect

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

from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import authenticate_user
from .models import *
from .serializer import *
from .tasks import *
from .form import create_customer,update_customer,update_picture
from roomapp.models import *
from django.core.files import File
from reservation.models import *
import datetime


def home_view(request):
    free_rooms =RoomModel.objects.filter(status='Free')
    context={'free_rooms':free_rooms, 'request':request}
    return render(request, 'home.html', context)

@login_required(login_url='login')
def dashboard(request):
    userr=CustomBaseuser.objects.get(email=request.user.email)
    reservations = ReservationModel.objects.filter(user=userr)
    count=reservations.count()
    context={'reservations':reservations,'count':count,'user':userr}
    return render(request,'dashboard.html',context)

@login_required(login_url='login')
def profile_view(request):
    userr=CustomBaseuser.objects.get(email=request.user.email)
    update_customer_form = update_customer(request.POST,instance=userr)
    update_picture_form = update_picture(request.POST,request.FILES,instance=userr)
    if request.method == "POST" and request.POST.get('type')=='update_picture':
        print(update_picture_form.data)
        update_picture_form = update_picture(request.POST,request.FILES,instance=userr)
        if update_picture_form.is_valid():
            print('pic')
            update_picture_form.save(commit=True)

    if request.method == "POST" and request.POST.get('type') == 'update_user_info':
        # pwd=request.POST.get('password')
        
        if update_customer_form.is_valid():
            print('valid')
            # userr.set_password(pwd)
            update_customer_form.save(commit=True)
            print(userr.firstname)
    if request.method == "POST" and request.POST.get('type') == 'update_password':
        current_pwd=request.POST.get('password')
        new_pwd = request.POST.get('new_password')
        check = userr.check_password(current_pwd)
        print(check)
        if check == True:
            userr.set_password(new_pwd)
            userr.save()
        

    if request.method == "POST" and request.POST.get('type') == 'delete':
        print('in')
        userr=CustomBaseuser.objects.get(email=request.user.email)
        userr.delete()
        request.user.delete()
        
    context={'details':request.user,
             'update_picture_form':update_picture_form,
             'update_customer_form':update_customer_form,}
    return render(request, 'Profile.html', context)

@authenticate_user
def signup_view(request):
    form = create_customer(request.POST)
    if request.method=="POST":
        CustomBaseuser.objects.create_user(request.POST.get('email'),
                                         request.POST.get('firstname'),
                                         request.POST.get('lastname'),
                                         request.POST.get('password'))
        return redirect('dashboard')
    context = {'form':form,'None':''}
    return render(request, 'signup.html', context)

@authenticate_user
def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user != None: 
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, "Username OR Password is incorrect") #you dont need to pass through context
    context = {}
    return render(request, 'login.html', context)

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')



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

