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

def reservation(request):
    basic_user = request.user
    user = CustomBaseuser.objects.filter(email=basic_user.email)
    free_rooms = RoomModel.objects.filter(status='Free')
    preference = Preferencemodel.objects.filter(user=user.first())
    if request.method=='POST':
        try:
            user = CustomBaseuser.objects.get(email=basic_user.email)
            preference = Preferencemodel.objects.get(user=user)
            payment=PaymentModel.objects.create(user=user,
                                    lastName=request.POST.get('lastname'),
                                    firstName=request.POST.get('firstname'),
                                    reference_id=request.POST.get('reference_id'),
                                    amount=request.POST.get('amount'),
                                    description=request.POST.get('description'),
                                    paymenttime = request.POST.get('paymenttime'))
            try:
                reservation = ReservationModel.objects.create(
                                                    user=user,
                                                        checkInDateandTime= request.POST.get('checkInDateandTime'),
                                                        preference_id = preference.pk,
                                                        payment=payment
                    )
                print(reservation)
                for room in request.POST.get('rooms'):
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
            except:
                print('op')
        except:
            print('p')
    context={'free_rooms':free_rooms,
             'preference':preference.first()}
    return render(request, 'reservation.html', context)

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
        

   



