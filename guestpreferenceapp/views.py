from django.shortcuts import render
from .models import Preferencemodel
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import Preferenceserializer
# Create your views here.

class PreferenceView(APIView):
    def post(self,request):
        data=request.data
        userpreference = Preferencemodel.objects.get(user__email=data['email'])
        serialized_userpreference = Preferenceserializer(instance=userpreference)
        if userpreference:
            return Response({'message':'Preference Exists'})
        
        else:
            return Response({'message':serialized_userpreference.data})
        
        
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
                return Response({'message':'Updated'})
            except:
                return Response({'message':'Check your data'})
        except:
            return Response({'message':'Please sign_up and createa a Preference'})