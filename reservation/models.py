from django.db import models
from Customeruser.models import CustomBaseuser
from roomapp.models import RoomModel
from guestpreferenceapp.models import Preferencemodel
from Payment.models import PaymentModel

# Create your models here.
class ReservationModel(models.Model):
    user=models.ForeignKey(CustomBaseuser,on_delete=models.CASCADE)
    checkInDateandTime= models.DateTimeField(auto_now_add=True, null=False,blank=False)
    preference=models.ForeignKey(Preferencemodel,on_delete=models.CASCADE)
    payment=models.OneToOneField(PaymentModel,on_delete=models.CASCADE,null=True,blank=False)
    def __str__(self):
        return f'{self.checkInDateandTime} {self.user.email} Reservation'
    
class ReservedRooms(models.Model):
    reservedroom=models.ForeignKey(ReservationModel, on_delete=models.CASCADE)
    room=models.OneToOneField(RoomModel,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.room.roomname}'