from typing import Any
from django.contrib import admin
from django.db.models.fields.related import ForeignKey
from django.forms.models import ModelChoiceField
from django.http.request import HttpRequest
from .models import *
from guestpreferenceapp.models import *

# Register your models here.
class ReservedRoomsAdmin(admin.StackedInline):
    model = ReservedRooms
    def formfield_for_foreignkey(self, db_field: ForeignKey[ReservedRooms], request: HttpRequest | None, **kwargs: Any) -> ModelChoiceField | None:
        if db_field.name=='room':
            kwargs["queryset"]= RoomModel.objects.filter(status='Free')
            return super().formfield_for_foreignkey(db_field, request, **kwargs)
        
    
    
@admin.register(ReservationModel)
class ReservationModelAdmin(admin.ModelAdmin):
    inlines = [ReservedRoomsAdmin]
    def formfield_for_foreignkey(self, db_field: ForeignKey[ReservationModel], request: HttpRequest | None, **kwargs: Any) -> ModelChoiceField | None:
        if db_field.name=='preference':
            kwargs["queryset"]= Preferencemodel.objects.filter(user=request.user)
    
        if db_field.name=='user':
            kwargs["queryset"]=CustomBaseuser.objects.filter(id=request.user.id)
        
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    

@admin.register(ReservedRooms)
class ReservedRoomsAdmin(admin.ModelAdmin):
    pass