from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import *
from .serializer import *
import json


# @api_view(['POST'])
# def roomupload(request):
#     if request.method == 'POST': 
#         name=request.POST.get('filename')# name and id of input should be 'filename'
#         myfile=request.FILES.getlist('uploadfiles')
#         print(myfile)
#         return Response({'message':'file'})
    
# View for List of Rooms
class Listroom(APIView,):
    permission_classes = [AllowAny,]
    parser_classes = [MultiPartParser, FormParser]
    def get(self, request):
        room=RoomModel.objects.all() 
        serialized_room_data=Room_list_serializer(room,many=True)
        return Response({'message':serialized_room_data.data})
        