from django.db import models
from reservation.models import *
from Customeruser.models import CustomBaseuser


class CheckoutModel(models.Model):
    user=models.ForeignKey(CustomBaseuser,on_delete=models.CASCADE,null=True)
    checkInDateandTime=models.CharField(max_length=150, blank=True,null=False)
    checkOutDateandTime= models.DateTimeField(auto_now_add=True, null=False)
    preference=models.CharField(max_length=150, blank=False,null=True)
    payment=models.CharField(max_length=150, blank=False,null=True)
    amount=models.CharField(max_length=150, blank=False,null=True)
    reference_id=models.CharField(max_length=150, blank=False,null=True)
    room=models.CharField(max_length=150, blank=False,null=True)
    def __str__(self):
        return f"Checkout for {self.user} at {self.checkOutDateandTime}"