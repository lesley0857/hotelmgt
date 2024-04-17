from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
import datetime
from django.contrib import messages
from Customeruser.models import CustomBaseuser
from guestpreferenceapp.models import Preferencemodel
from roomapp.models import RoomModel
from .models import ReservationModel,ReservedRooms
from .serializer import Reservation_list_serializer
from Payment.models import PaymentModel
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def success_view(request):
    basic_user = request.user
    user = CustomBaseuser.objects.get(email=basic_user.email)
    reservation= ReservationModel.objects.last()
    payment = PaymentModel.objects.last()
    preference = Preferencemodel.objects.filter(user=user).first()
    checkout_time = reservation.checkInDateandTime  + datetime.timedelta(days=int(reservation.numberofdays))
    print(preference.bedspread)
    messages.success(request,"Reservation Created")
    context={'checkout_time':checkout_time,
             'user':user,'reservation':reservation,'payment':payment,
             'preference':preference}
    return render(request, 'success.html', context)

@login_required(login_url='login')
def reservation_id(request,id):
    basic_user = request.user
    user = CustomBaseuser.objects.get(email=basic_user.email)
    reservation= ReservationModel.objects.get(id=id)
    payment_id = reservation.payment.pk
    payment = PaymentModel.objects.get(id=payment_id)
    preference = Preferencemodel.objects.filter(user=user).last()
    checkout_time = reservation.checkInDateandTime  + datetime.timedelta(days=int(reservation.numberofdays))
    print(preference.bedspread)
    context={'checkout_time':checkout_time,
             'user':user,'reservation':reservation,'payment':payment,
             'preference':preference}
    return render(request, 'reservation_id.html', context)


@login_required(login_url='login')
def reservation(request):
    basic_user = request.user
    user = CustomBaseuser.objects.get(email=basic_user.email)
    free_rooms = RoomModel.objects.filter(status='Free')
    rooms = RoomModel.objects.all()
    preference = Preferencemodel.objects.filter(user=user)
    number_of_days_to_spend = request.POST.get('days_count')
    print(rooms)
    status_context=''
    if request.method=='POST':
        status = RoomModel.objects.get(roomname=request.POST.get('free_rooms'))
        print(request.POST.get('heater'))
        year = request.POST.get('checkInDateandTime').split('-')[0]
        month= request.POST.get('checkInDateandTime').split('-')[1]
        day = request.POST.get('checkInDateandTime').split('-')[2].split('T')[0]
        
        potential_checkin = request.POST.get('checkInDateandTime').split('-')[2].split('T')[0]         
        reservation_list= ReservationModel.objects.filter(room=request.POST.get('free_rooms'))
        reservation = reservation_list.last()
        print(reservation)
        if reservation is None:
            print('Reservation is None')
            status_context='Free'
            if request.POST.get('determinant')=='Create':
                room_booked = RoomModel.objects.get(roomname=request.POST.get('free_rooms'))
                preferencemodel_count = Preferencemodel.objects.filter(user_id=user.pk).count()
            
                if preferencemodel_count <= 0:

                    preferencemodel = Preferencemodel.objects.create(user=user,
                                                   lighting=request.POST.get('Lighting'),
                                                   bedspread=request.POST.get('Bedspread'),
                                                   heater=request.POST.get('heater'),
                                                   airconditioner=request.POST.get('airconditioner'))
                    preferencemodel.save()
                    payment=PaymentModel.objects.create(user=user,
                                        lastName=user.lastname,
                                        firstName=user.firstname,
                                        reference_id='1234abc', # random number
                                        amount=int(room_booked.price) * int(number_of_days_to_spend),
                                        description=f" for {request.POST.get('free_rooms')}",
                                        paymenttime = request.POST.get('checkInDateandTime'))
                    print(request.POST.get('checkInDateandTime'))
                    preference=Preferencemodel.objects.filter(user=user)
                    reservation = ReservationModel.objects.create(
                                                    user=user,
                                                    room=request.POST.get('free_rooms'),
                                                    payment=payment,
                                                    numberofdays=request.POST.get('days_count'),
                                                        checkInDateandTime= request.POST.get('checkInDateandTime'),
                                                        preference = preferencemodel                                   
                    )
                    roommodel=RoomModel.objects.get(roomname=request.POST.get('free_rooms'))
                    roommodel.status='Occupied'
                    roommodel.save()
                    messages.success(request,"Reservation Created")
                    context={'free_rooms':free_rooms,'rooms':rooms,
                    'preference':preference.first()}
                    return redirect('success')
                
                else:
                    preferencemodel = Preferencemodel.objects.filter(user=user)[0]
                    preferencemodel.lighting = request.POST.get('Lighting'),
                    preferencemodel.bedspread = request.POST.get('Bedspread'),
                    preferencemodel.heater= request.POST.get('heater'),
                    preferencemodel.airconditioner = request.POST.get('airconditioner'),
                    
                    payment=PaymentModel.objects.create(user=user,
                                        lastName=user.lastname,
                                        firstName=user.firstname,
                                        reference_id='1234abc', # random number
                                        amount=int(room_booked.price) * int(number_of_days_to_spend),
                                        description=f" for {request.POST.get('free_rooms')}",
                                        paymenttime = request.POST.get('checkInDateandTime'))
                    print(request.POST.get('checkInDateandTime'))
                    
                    reservation = ReservationModel.objects.create(
                                                    user=user,
                                                    payment=payment,
                                                    room=request.POST.get('free_rooms'),
                                                    numberofdays=request.POST.get('days_count'),
                                                        checkInDateandTime= request.POST.get('checkInDateandTime'),
                                                        preference = preferencemodel                             
                    )
                    roommodel=RoomModel.objects.get(roomname=request.POST.get('free_rooms'))
                    roommodel.status='Occupied'
                    roommodel.save()
                    messages.success(request,"Reservation Created")
                    context={'free_rooms':free_rooms,'rooms':rooms,
                    'preference':preference.first()}
                    return redirect('success')
                        
            if request.POST.get('determinant')=='Check':
                messages.success(request,f"{request.POST.get('free_rooms')} is free on {day}/{month}/{year}")
                context={'free_rooms':free_rooms,'rooms':rooms,'status_context':status_context,
                'preference':preference.first()}
                return render(request, 'reservation.html', context)
        else:
            print("reservation is not None")
            checkout_time = reservation.checkoutime()
            if status.status=='Free' or int(potential_checkin) > checkout_time.day:
                status_context='Free'
                if request.POST.get('determinant')=='Create':
                    room_booked = RoomModel.objects.get(roomname=request.POST.get('free_rooms'))
                    preferencemodel_count = Preferencemodel.objects.filter(user_id=user.pk).count()
                
                    if preferencemodel_count <= 0:

                        preferencemodel = Preferencemodel.objects.create(user=user,
                                                    lighting=request.POST.get('Lighting'),
                                                    bedspread=request.POST.get('Bedspread'),
                                                    heater=request.POST.get('heater'),
                                                    airconditioner=request.POST.get('airconditioner'))
                        
                        payment=PaymentModel.objects.create(user=user,
                                            lastName=user.lastname,
                                            firstName=user.firstname,
                                            reference_id='1234abc', # random number
                                            amount=int(room_booked.price) * int(number_of_days_to_spend),
                                            description=f" for {request.POST.get('free_rooms')}",
                                            paymenttime = request.POST.get('checkInDateandTime'))
                        print(request.POST.get('checkInDateandTime'))
                        preference=Preferencemodel.objects.filter(user=user)
                        reservation = ReservationModel.objects.create(
                                                        user=user,
                                                        room=request.POST.get('free_rooms'),
                                                        payment=payment,
                                                        numberofdays=request.POST.get('days_count'),
                                                            checkInDateandTime= request.POST.get('checkInDateandTime'),
                                                            preference = preferencemodel                                   
                        )
                        roommodel=RoomModel.objects.get(roomname=request.POST.get('free_rooms'))
                        roommodel.status='Occupied'
                        roommodel.save()
                        messages.success(request,"Reservation Created")
                        context={'free_rooms':free_rooms,'rooms':rooms,
                        'preference':preference.first()}
                        return redirect('success')
                    
                    else:
                        preferencemodel = Preferencemodel.objects.filter(user=user).last()
                        print(preferencemodel.lighting)
                        preferencemodel.delete()
                        preferencemodel.objects.create(user=user,
                                                    lighting=request.POST.get('Lighting'),
                                                    bedspread=request.POST.get('Bedspread'),
                                                    heater=request.POST.get('heater'),
                                                    airconditioner=request.POST.get('airconditioner'))
                        
                        payment=PaymentModel.objects.create(user=user,
                                            lastName=user.lastname,
                                            firstName=user.firstname,
                                            reference_id='1234abc', # random number
                                            amount=int(room_booked.price) * int(number_of_days_to_spend),
                                            description=f" for {request.POST.get('free_rooms')}",
                                            paymenttime = request.POST.get('checkInDateandTime'))
                        print(request.POST.get('checkInDateandTime'))
                        
                        reservation = ReservationModel.objects.create(
                                                        user=user,
                                                        payment=payment,
                                                        room=request.POST.get('free_rooms'),
                                                        numberofdays=request.POST.get('days_count'),
                                                            checkInDateandTime= request.POST.get('checkInDateandTime'),
                                                            preference = preferencemodel                             
                        )
                        roommodel=RoomModel.objects.get(roomname=request.POST.get('free_rooms'))
                        roommodel.status='Occupied'
                        roommodel.save()
                        messages.success(request,"Reservation Created")
                        context={'free_rooms':free_rooms,'rooms':rooms,
                        'preference':preference.first()}
                        return redirect('success')
                            
                if request.POST.get('determinant')=='Check':
                    messages.success(request,f"{request.POST.get('free_rooms')} is Free on {day} of {month} {year}")
                    context={'free_rooms':free_rooms,'rooms':rooms,'status_context':status_context,
                    'preference':preference.first()}
                    return render(request, 'reservation.html', context)
            else:
                reservation_list= ReservationModel.objects.filter(room=request.POST.get('free_rooms'))
                reservation = reservation_list.last()
                checkout_time = reservation.checkoutime()            
                
                if datetime.datetime.now().day >= checkout_time.day:
                    room = RoomModel.objects.get(roomname=request.POST.get('free_rooms'))
                    room.status = 'Free'
                    room.save()
                    messages.success(request,f"{room} is Free")
                else:
                    status_context='Occupied'
                    messages.success(request,f"""{request.POST.get('free_rooms')} is Occupied, would be free by
                                {checkout_time.ctime()}""")
                    context={'free_rooms':free_rooms,'rooms':rooms,'status_context':status_context,
                        'preference':preference.first()}
                    return render(request, 'reservation.html', context)
            
    context={'free_rooms':free_rooms,'rooms':rooms,'status_context':status_context,
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
        

   



