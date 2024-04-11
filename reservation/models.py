from django.db import models
from Customeruser.models import CustomBaseuser
from roomapp.models import RoomModel
from guestpreferenceapp.models import Preferencemodel
from Payment.models import PaymentModel
import datetime

# Create your models here.
class ReservationModel(models.Model):
    user=models.ForeignKey(CustomBaseuser,on_delete=models.CASCADE)
    checkInDateandTime= models.DateTimeField(auto_now_add=True, null=False,blank=False)
    preference=models.ForeignKey(Preferencemodel,on_delete=models.CASCADE,null=True)
    numberofdays = models.CharField(max_length=150, blank=False,null=True)
    payment=models.OneToOneField(PaymentModel,on_delete=models.CASCADE,null=True,blank=True)
    room = models.CharField(max_length=150, blank=False,null=True)
    def __str__(self):
        return f'{self.checkInDateandTime} {self.user.email} Reservation'
    
    def checkoutime(self):
        return self.checkInDateandTime + datetime.timedelta(days=int(self.numberofdays))

class ReservedRooms(models.Model):
    reservedroom=models.ForeignKey(ReservationModel, on_delete=models.CASCADE)
    room=models.OneToOneField(RoomModel,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.room.roomname}'