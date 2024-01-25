from django.shortcuts import render
from .models import Preferencemodel
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import Preferenceserializer
from Customeruser.models import CustomBaseuser
# Create your views here.

class PreferenceView(APIView):
    def get(self,request,email):
        try:
            userpreference = Preferencemodel.objects.get(user__email=email)
            if userpreference:
                serialized_userpreference = Preferenceserializer(instance=userpreference)
                return Response({'message':serialized_userpreference.data})
            
            else:
                return Response({'message':'Please create a Preference'})
        except:
            return Response({'message':'Preference Does Not Exists'})

            
    def post(self,request):
        data=request.data
        try:
            userpreference = Preferencemodel.objects.get(user__email=data['email'])
            return Response({'message':'Preference Exists'})
                
        except:
            try:
                    user=CustomBaseuser.objects.get(email=data['email'])
                    Preferencemodel.objects.create(user_id=user.pk,
                                                   lighting=data['lighting'],
                                                   bedspread=data['bedspread'],
                                                   heater=data['heater'],
                                                   airconditioner=data['airconditioner'])
                    return Response({'message':'Created'})
            except:
                return Response({'message':'No user with such email'})
        
        
    def put(self,request):
        data=request.data
        try:
            updated_preference = Preferencemodel.objects.get(user__email=data['email'])
            try:     
                data['lighting'],data['airconditioner'],data['bedspread'],data['heater']
                
                updated_preference.lighting=data['lighting']
                updated_preference.airconditioner=data['airconditioner']
                updated_preference.bedspread=data['bedspread']
                updated_preference.heater=data['heater']
                updated_preference.save()
                return Response({'message':'Updated'})
            except:
                return Response({'message':'Check your data'})
        except:
            return Response({'message':'Please sign_up and create a Preference'})