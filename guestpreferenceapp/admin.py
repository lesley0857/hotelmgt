from django.contrib import admin
from django.db.models.fields.related import ForeignKey
from django.forms.models import ModelChoiceField
from django.http.request import HttpRequest
from typing import Any
from .models import *
from Customeruser.models import CustomBaseuser



@admin.register(Preferencemodel)
class PreferenceModelAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field: ForeignKey[Preferencemodel], request: HttpRequest | None, **kwargs: Any) -> ModelChoiceField | None:
        if db_field.name=='user':
            kwargs["queryset"]= CustomBaseuser.objects.filter(id=request.user.id)
            return super().formfield_for_foreignkey(db_field, request, **kwargs)
      