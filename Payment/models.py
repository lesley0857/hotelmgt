from django.db import models
from Customeruser.models import CustomBaseuser


class PaymentModel(models.Model):
    user = models.ForeignKey(
        CustomBaseuser, models.CASCADE, null=True, blank=False)
    lastName = models.CharField(max_length=150, blank=False)
    firstName = models.CharField(max_length=150, blank=False)
    reference_id = models.CharField(max_length=150, blank=False)
    amount = models.IntegerField(blank=False)
    description = models.TextField(max_length=150, blank=False)
    paymenttime = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.email}---N{self.amount} FOR {self.reference_id}'
