from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from Customeruser.models import CustomBaseuser
from .models import ReservationModel,ReservedRooms
from .serializer import Reservation_list_serializer

class ReservationView(APIView):
    def get(self,request):
        data = request.data
        try:
            user = CustomBaseuser.objects.get(user__email=data['email'])
            try:
                reservation = ReservationModel.objects.filter(user__id=user.pk)
                serialized_reservation=Reservation_list_serializer(reservation,many=True)
                return Response({'message':serialized_reservation.data})
            except:
                return Response({'message':'Please Create a Reservation'})
        except:
            return Response({'message':'Please Signup to create a reservation'})
        # Must be called after payment is verified
    def post(self,request):
        data = request.data
        try:
            user = CustomBaseuser.objects.get(user__email=data['email'])
            try:
                reservation = ReservationModel.objects.create(
                                                    user__email=data['email'],
                                                    checkInDateandTime= data['checkInDateandTime'],
                                                    preference = data['preference']
                )
                for room in data['rooms']:
            # rooms field from the frontend should be a list of available rooms.You can loop through the list
                    reserved_rooms = ReservedRooms.objects.create(reservedroom__id=reservation.pk,
                                                              room=room)
                return Response({'message':'Reservation Created'})
            except:
                return Response({'message':'Please Create a Reservation'})
        except:
            return Response({'message':'Please Signup to create a reservation'})
        #  create a function for adding rooms to a particular reservation
        #create a function for removing rooms to a particular reservation
   



