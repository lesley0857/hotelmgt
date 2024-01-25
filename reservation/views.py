from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from Customeruser.models import CustomBaseuser
from guestpreferenceapp.models import Preferencemodel
from roomapp.models import RoomModel
from .models import ReservationModel,ReservedRooms
from .serializer import Reservation_list_serializer
from Payment.models import PaymentModel

class ReservationView(APIView):
    def get(self,request,email):
        try:
            user = CustomBaseuser.objects.get(email=email)
            try:
                reservation = ReservationModel.objects.filter(user=user)
                serialized_reservation=Reservation_list_serializer(reservation,many=True)
                return Response({'message':serialized_reservation.data})
            except:
                return Response({'message':'Please Create a Reservation'})
        except:
            return Response({'message':'Please Signup to create a reservation'})
        
        
    def post(self,request):
        data = request.data
        try:
            user = CustomBaseuser.objects.get(email=data['email'])
            preference = Preferencemodel.objects.get(user=user)
            payment=PaymentModel.objects.create(user=user,
                                    lastName=data['lastname'],
                                    firstName=data['firstname'],
                                    reference_id=data['reference_id'],
                                    amount=data['amount'],
                                    description=data['description'],
                                    paymenttime = data['paymenttime'])
            try:
                reservation = ReservationModel.objects.create(
                                                   user=user,
                                                    checkInDateandTime= data['checkInDateandTime'],
                                                    preference_id = preference.pk,
                                                    payment=payment
                )
                print(reservation)
                for room in data['rooms']:
                    print(room)
                    room_model=RoomModel.objects.get(roomname=room['room'])
                    print(room_model)
                    reserved_rooms = ReservedRooms.objects.create(reservedroom=reservation,
                                                              room = room_model
                                                              )
                    print(reserved_rooms.room.status)
                    a=RoomModel.objects.get(roomname=reserved_rooms)
                    a.status='Occupied'
                    a.save()
                return Response({'message':'Reservation Created'})
            except:
                return Response({'message':'Reservation Exists'})
        except:
            return Response({'message':'Please create a Preference and Signup to create a reservation'})
        

   



