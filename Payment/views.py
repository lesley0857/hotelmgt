from django.shortcuts import render,redirect
import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from Customeruser.models import CustomBaseuser
from Payment.models import PaymentModel

# Create your views here.
''' send in reservation field and payment field details through the request
    then create payment object then make API call to create the 
    reservation object '''
# res=requests.get('http://127.0.0.1:8000/api/reserve/lesley@gmail.com')
# print(res.json())

@login_required(login_url='login')
def payment(request):
    if request.method=='POST':
        userr = CustomBaseuser.objects.get(email=request.user.email)
        PaymentModel.objects.create(user=userr,
                                    lastName = userr.lastname,
                                    firstName = userr.firstname,
                                    reference_id = '12',
                                    amount = '300',
                                    description='for 3 rooms',
                                    paymenttime=request.POST.get('paymenttime'))
        # return redirect('reservation')
    context = {}
    return render(request, 'payment.html', context)

class PaymentView(APIView):
    def post(self,request):
        dataa = request.data
        user = CustomBaseuser.objects.get(email=dataa['email'])
        payment=PaymentModel.objects.create(user=user,
                                    lastName=dataa['lastname'],
                                    firstName=dataa['firstname'],
                                    reference_id=dataa['reference_id'],
                                    amount=dataa['amount'],
                                    description=dataa['description'],
                                    paymenttime = dataa['paymenttime'])
        requests.post(url='http://127.0.0.1:8000/api/reservation',
                            data={ "email":dataa['email'],
                                "checkInDateandTime":dataa['checkInDateandTime'],
                                "rooms":dataa['rooms'],'payment':payment
                        })
        return Response({'message':'Payment Created'})
