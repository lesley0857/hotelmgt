from django.db import models

# Create your models here.

class RoomModel(models.Model):
    STATUS = (('Free', 'Free'), ('Occupied',
              'Occupied'),)
    roomname= models.CharField(max_length=150, blank=False)
    cardNo= models.CharField(max_length=150, blank=False)
    status= models.CharField(
        max_length=200, choices=STATUS, default='STATUS[0]', blank=False, null=False)
    price= models.CharField(max_length=150, blank=False,null=True)
    persons = models.CharField(max_length=150, blank=False,null=True)
    wifi = models.BooleanField(default=False,null=True)
    kitchen = models.BooleanField(default=False,null=True)
    bathroom = models.BooleanField(default=False,null=True)
    profile_pic = models.ImageField(default="/Koala.jpg/",null=True)
    def __str__(self):
        return f'{self.roomname}'

    
class RoomfileModel(models.Model):
    roommodel=models.ForeignKey(RoomModel, on_delete=models.CASCADE)
    file = models.FileField(upload_to='images', null = True, blank = True)
    def __str__(self):
        return f'{self.roommodel}--{self.file.name}'