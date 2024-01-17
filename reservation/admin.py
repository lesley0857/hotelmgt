from django.contrib import admin
from .models import *

# Register your models here.
class ReservedRoomsAdmin(admin.StackedInline):
    model = ReservedRooms

@admin.register(ReservationModel)
class ReservationModelAdmin(admin.ModelAdmin):
    inlines = [ReservedRoomsAdmin]

@admin.register(ReservedRooms)
class ReservedRoomsAdmin(admin.ModelAdmin):
    pass