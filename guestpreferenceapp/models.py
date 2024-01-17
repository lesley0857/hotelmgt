from django.db import models
from Customeruser.models import CustomBaseuser

# Create your models here.
class Preferencemodel(models.Model):
    LIGHT_CHOICE = (('chandelier', 'chandelier'), ('Pendant Light','Pendant Light'),
                    ('Track Light','Track Light'),('Cabinet Light','Cabinet Light'),
                    ('Accent Light','Accent Light'),('Ceiling Light','Ceiling Light'),)
    BEDSPREAD_CHOICE = (('Quilts,Coverlets,Blankets,Throwers,3-Pillows', 'Quilts,Coverlets,Blankets,Throwers,3-Pillows'), 
                        ('Coverlets,Blankets,Throwers,3-Pillows','Coverlets,Blankets,Throwers,3-Pillows'),
                        ('Coverlets,Blankets,2-Pillows','Coverlets,Blankets,2-Pillows'),
                        ('Coverlets,Throwers,3-Pillows','Coverlets,Throwers,3-Pillows'),)
    
    user=models.OneToOneField(CustomBaseuser,on_delete=models.CASCADE)
    lighting=models.CharField(max_length=400, choices=LIGHT_CHOICE, default='STATUS[0]', blank=False, null=True)
    bedspread = models.CharField(max_length=400, choices=BEDSPREAD_CHOICE, default='STATUS[0]', blank=False, null=True)
    heater = models.BooleanField(default=False)
    airconditioner = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.lastname} {self.user.firstname}'s Preference"
