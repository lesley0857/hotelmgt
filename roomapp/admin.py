from django.contrib import admin
from .models import RoomModel, RoomfileModel
# Register your models here.

# admin.site.register(RoomModel)

class RoomFileAdmin(admin.StackedInline):
    model = RoomfileModel

@admin.register(RoomModel)
class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomFileAdmin]

@admin.register(RoomfileModel)
class RoomFileAdmin(admin.ModelAdmin):
    pass