from django.contrib import admin
from typing import Any
from django.contrib import admin
from django.db.models.fields.related import ForeignKey
from django.forms.models import ModelChoiceField
from django.http.request import HttpRequest
from .models import *
from reservation.models import ReservationModel
# Register your models here.

@admin.register(CheckoutModel)
class CheckoutModelAdmin(admin.ModelAdmin):
    
    def formfield_for_foreignkey(self, db_field: ForeignKey[CheckoutModel], request: HttpRequest | None, **kwargs: Any) -> ModelChoiceField | None:
        if db_field.name=='reservation':
            kwargs["queryset"]= ReservationModel.objects.filter(user=request.user)
      
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
