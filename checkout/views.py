from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from Customeruser.models import CustomBaseuser
from reservation.models import ReservationModel,ReservedRooms
from .models import CheckoutModel
from roomapp.models import *

class CheckoutView(APIView):
    def post(self,request):
        data = request.data
        try:
            user = CustomBaseuser.objects.get(email=data['email'])
            try:
                reservation=ReservationModel.objects.get(id=data['reservation'])
                print(reservation)
                room=ReservedRooms.objects.filter(reservedroom=reservation)
                print(room)
                # Create Checkout to keep record of user reservation, payment and checkout
                CheckoutModel.objects.create(user=user,
                                             checkInDateandTime=reservation.checkInDateandTime,
                                             checkOutDateandTime=data['checkOutDateandTime'],
                                             preference=reservation.payment,
                                             payment=reservation.payment,
                                             amount=reservation.payment.amount,
                                             reference_id=reservation.payment.reference_id,
                                             room=f'{room}')
                # Reset room status to 'Free'
                for i in room:
                    c = RoomModel.objects.get(roomname=i.room)
                    c.status="Free"
                    c.save()
                # Delete Reservation
                reservation.delete()

                return Response({'message':'Created'})
            except:
                return Response({'message':'No Reservation to check-out'})
        except:
                return Response({'message':'Please Log-in'})
